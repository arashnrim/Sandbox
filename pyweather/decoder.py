import configparser
import json
import sys
from urllib import request, error

parser = configparser.ConfigParser()


class NoConfigError(Exception):
    pass


def retrieve_default_location():
    try:
        data = parser.read("config.ini")
        if not data:
            raise NoConfigError
    except NoConfigError:
        sys.exit("No config file found or there was an invalid file. Ending execution.")
    else:
        default_location = parser["Config"]["defaultLocation"]

    if default_location:
        return default_location
    else:
        return ""


def retrieve_data(location):
    try:
        data = parser.read("config.ini")
        if not data:
            raise NoConfigError
    except NoConfigError:
        sys.exit("No config file found or there was an invalid file. Ending execution.")
    else:
        api_key = parser["Config"]["apiKey"]

    try:
        # noinspection SpellCheckingInspection
        with request.urlopen(
                "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location, api_key)) as url:
            data = json.load(url)
            return data
    except error.URLError as httpError:
        print(httpError.reason)
