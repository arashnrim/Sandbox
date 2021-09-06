import configparser
import json
import os
import sys
from urllib import request, error

from styling import Style

parser = configparser.ConfigParser()
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class NoConfigError(Exception):
    pass


def retrieve_default_location():
    try:
        data = parser.read("{}/config.ini".format(ROOT_DIR))
        if not data:
            raise NoConfigError
    except NoConfigError:
        sys.exit("No config file found or there was an invalid file. Ending execution.")
    else:
        default_location = parser["DEFAULT"]["defaultlocation"]

    if default_location:
        return default_location
    else:
        return ""


def retrieve_data(location):
    try:
        data = parser.read("{}/config.ini".format(ROOT_DIR))
        if not data:
            raise NoConfigError
    except NoConfigError:
        sys.exit("No config file found or there was an invalid file. Ending execution.")
    else:
        api_key = parser["DEFAULT"]["apikey"]

    try:
        # noinspection SpellCheckingInspection
        with request.urlopen(
                "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location, api_key)) as url:
            data = json.load(url)
            return data
    except error.HTTPError as httpError:
        print(
            "{}An error occurred; a {}{} response code{}{} was given. Please try again.{}".format(Style.RED, Style.BOLD,
                                                                                                  httpError.code,
                                                                                                  Style.END, Style.RED,
                                                                                                  Style.END))
