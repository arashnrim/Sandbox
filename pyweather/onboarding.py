import configparser
import os
from pathlib import Path
from time import sleep

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

"""
Welcomes the user to the project and guides them through on-boarding.
"""


def welcome():
    print(
        "Welcome to pyweather, a command-line weather tool to get information about the weather right from your "
        "terminal.",
        end="\n\n")
    sleep(1)
    while True:
        print(
            "Would you like to save pyweather to your rc file? This allows you to run 'weather' at any time in your "
            "terminal.",
            end=" ")
        save = input("(y/n): ")
        if save == "y" or save == "Y":
            save_in_path_completion(save_in_path())
            break
        elif save == "n" or save == "N":
            break
        else:
            print("Invalid. Save pyweather to rc file?", end=" ")
    sleep(1)
    while True:
        print("Would you like to set a default location? pyweather will always try this location first.", end=" ")
        default = input("(y/n): ")
        if default == "y" or save == "Y":
            save_default()
            break
        elif save == "n" or save == "N":
            break
        else:
            print("Invalid. Set a default location?", end=" ")
    sleep(1)
    while True:
        api_key = input("Enter your OpenWeatherMap API key now: ")
        if len(api_key) == 32:
            save_api_key(api_key)
            break
        else:
            print("Invalid.", end=" ")
    sleep(1)
    print()
    print("That's it. Thanks for setting up!", end="\n\n")


"""
Saves the program execution in the user's rc path via an alias.

The function attempts to detect the shell environment and saves the alias based on the rc file of the shell.
"""


def save_in_path():
    profile = ""
    shell = os.environ['SHELL']
    if shell == "/bin/zsh":
        profile = "{}/.zshrc".format(Path.home())
    elif shell == "/bin/bash":
        profile = "{}/.bashrc".format(Path.home())

    try:
        rc = open(profile, "a")
        rc.write("\nalias weather=\"python3 {}\"".format(ROOT_DIR))
        rc.close()
    except OSError:
        return False
    else:
        return True


"""
A work-around completion handler to execute after save_in_path() has concluded.
"""


def save_in_path_completion(status):
    if status:
        print("Operation successful!", end="\n\n")
    else:
        print("Something went wrong. Please try again later.", end="\n\n")


"""
Saves a default location for pyweather to run on every occurrence.
"""


def save_default():
    config = open("{}/config.ini".format(ROOT_DIR), "a")
    parser = configparser.ConfigParser()

    location = input("Enter the location name: ")
    parser.set("", "defaultlocation", location)
    parser.write(config)
    config.close()


"""
Saves the user's API key into the config.ini file.
"""


def save_api_key(api_key):
    config = open("{}/config.ini".format(ROOT_DIR), "a")
    parser = configparser.ConfigParser()

    parser.set("", "apikey", api_key)
    parser.write(config)
    config.close()
