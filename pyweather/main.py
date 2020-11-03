import argparse
import configparser
import os
from time import sleep

from art import tprint

from onboarding import welcome
from parse import parse
from request import retrieve_data, retrieve_default_location
from styling import Style

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
AP_PARSER = argparse.ArgumentParser()
AP_PARSER.add_argument("-l", "--location", help="get weather information for a custom location", dest="location")
AP_PARSER.add_argument("-nr", "--norepeat", help="do not prompt for re-entry", action="store_true", dest="norepeat")
AP_PARSER.add_argument("-nh", "--noheader", help="do not show pyweather header", action="store_true", dest="noheader")
AP_ARGS = AP_PARSER.parse_args()

# Tries to read if the user has set up the program before.
# Otherwise, the user is directed to onboarding.
try:
    parser = configparser.ConfigParser()
    parser.read("{}/config.ini".format(ROOT_DIR))
    api_key = parser["DEFAULT"]["apikey"]
except (OSError, KeyError):
    configured = False
else:
    configured = True

if not AP_ARGS.noheader:
    print("{}==========================".format(Style.BOLD))
    tprint("pyweather")
    print("=========================={}".format(Style.END), end="\n\n")

if not configured:
    sleep(2)
    welcome()

use_default_location = True
repeat = "y"
while repeat == "y" or repeat == "Y":
    if not AP_ARGS.location:
        if use_default_location:
            default_location = retrieve_default_location()
            if default_location != "":
                data = retrieve_data(default_location)
        else:
            location = input("Enter a location: ")
            data = retrieve_data(location)
    else:
        data = retrieve_data(AP_ARGS.location)

    # noinspection PyUnboundLocalVariable
    if data is not None:
        country_code = data["sys"]["country"]

        # noinspection PyUnboundLocalVariable,PyUnboundLocalVariable
        if not AP_ARGS.location:
            print("=== {}Weather for {}, {}{} ===".format(Style.BOLD,
                                                          default_location if use_default_location else location,
                                                          country_code, Style.END))
        else:
            print("=== {}Weather for {}, {}{} ===".format(Style.BOLD,
                                                          AP_ARGS.location,
                                                          country_code, Style.END))
        parse(data)

    if AP_ARGS.norepeat:
        break

    sleep(4)
    repeat = input("\nEnter another location? (y/n): ")
    if repeat == "y" or "Y":
        use_default_location = False
        AP_ARGS.location = ""
    else:
        break
