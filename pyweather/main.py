from time import sleep
import configparser
import os

from art import tprint

from decoder import retrieve_data, retrieve_default_location
from onboarding import welcome
from styling import Color
import weatherart

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
        # noinspection PyUnboundLocalVariable,PyUnboundLocalVariable
        print("=== {}Weather for {}{} ===".format(Color.BOLD, default_location if use_default_location else location,
                                                  Color.END))
        temp = round(data["main"]["temp"] / 10, 2)
        condition = data["weather"][0]["description"].capitalize()
        feels_like = round(data["main"]["feels_like"] / 10, 2)
        wind_direction = data["wind"]["deg"]
        wind_speed = data["wind"]["speed"]
        if condition == "Clear sky":
            weatherart.clear_sky()
        elif condition == "Few clouds":
            weatherart.few_clouds()
        elif condition == "Scattered clouds":
            weatherart.scattered_clouds()
        elif condition == "Broken clouds":
            weatherart.broken_clouds()
        elif condition == "Shower rain" or condition == "Rain":
            weatherart.rain()
        elif condition == "Thunderstorm":
            weatherart.thunderstorm()
        elif condition == "Snow":
            weatherart.snow()
        elif condition == "Mist":
            weatherart.mist()
        print("{}Current condition:{} {}".format(Color.YELLOW, Color.END, condition))
        print("{}Temperature:{} {}°C".format(Color.YELLOW, Color.END, temp))
        print("{}Feels like:{} {}°C".format(Color.YELLOW, Color.END, temp))
        if wind_direction == 0:
            wind_direction_arrow = "→"
        elif 0 < wind_direction < 90:
            wind_direction_arrow = "↗"
        elif wind_direction == 90:
            wind_direction_arrow = "↑"
        elif 90 < wind_direction < 180:
            wind_direction_arrow = "↖"
        elif wind_direction == 180:
            wind_direction_arrow = "←"
        elif 180 < wind_direction < 270:
            wind_direction_arrow = "↙"
        elif wind_direction == 270:
            wind_direction_arrow = "↓"
        elif 270 < wind_direction < 360:
            wind_direction_arrow = "↘"
        # noinspection PyUnboundLocalVariable
        print("{}Wind:{} {} {}m/s".format(Color.YELLOW, Color.END, wind_direction_arrow, wind_speed))
        sleep(4)
    repeat = input("\nEnter another location? (y/n): ")
    if repeat == "y" or "Y":
        use_default_location = False
    else:
        break
