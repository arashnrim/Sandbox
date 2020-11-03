import configparser
import os
from time import sleep

from art import tprint

from request import retrieve_data, retrieve_default_location
from onboarding import welcome
from styling import Color
from parse import parse

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

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

print("{}==========================".format(Color.BOLD))
tprint("pyweather")
print("=========================={}".format(Color.END), end="\n\n")

if not configured:
    sleep(2)
    welcome()

sleep(0.5)
use_default_location = True
repeat = "y"
while repeat == "y" or repeat == "Y":
    if use_default_location:
        default_location = retrieve_default_location()
        if default_location != "":
            data = retrieve_data(default_location)
    else:
        location = input("Enter a location: ")
        data = retrieve_data(location)

    # noinspection PyUnboundLocalVariable
    if data is not None:
        country_code = data["sys"]["country"]

        # noinspection PyUnboundLocalVariable,PyUnboundLocalVariable
        print("=== {}Weather for {}, {}{} ===".format(Color.BOLD, default_location if use_default_location else location,
                                                      country_code, Color.END))
        parse(data)
        sleep(4)
    repeat = input("\nEnter another location? (y/n): ")
    if repeat == "y" or "Y":
        use_default_location = False
    else:
        break
