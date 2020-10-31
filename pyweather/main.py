from time import sleep

from art import tprint

from decoder import retrieve_data, retrieve_default_location
from onboarding import welcome
from styling import Color

# Tries to read if the user has set up the program before.
# Otherwise, the user is directed to on-boarding.
try:
    config = open("config.ini", "r")
except OSError:
    configured = False
else:
    configured = True

print("{}==========================".format(Color.BOLD))
tprint("pyweather")
print("=========================={}".format(Color.END), end="\n\n")

if not configured:
    sleep(2)
    welcome()
else:
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

        condition = data["weather"][0]["description"].capitalize()
        temp = round(data["main"]["temp"] / 10, 2)
        feels_like = round(data["main"]["feels_like"] / 10, 2)
        wind_direction = data["wind"]["deg"]
        wind_speed = data["wind"]["speed"]
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
        print("{}Wind:{} {} {}m/s".format(Color.YELLOW, Color.END, wind_direction_arrow, wind_speed))

        sleep(4)
        repeat = input("\nEnter another location? (y/n): ")
        if repeat == "y" or "Y":
            use_default_location = False
        else:
            break
