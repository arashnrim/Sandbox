from time import sleep
import os
from pathlib import Path
import configparser

"""
Welcomes the user to the project and guides them through on-boarding.
"""


def welcome():
    print(
        "Welcome to pyweather, a command-line weather tool to get information about the weather right from your "
        "terminal.",
        end="\n\n")
    sleep(2)
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
    sleep(2)
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
    sleep(2)
    print()
    print("That's it. Thanks for setting up!")


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
        root_dir = os.path.dirname(os.path.abspath(__file__))
        rc.write("\nalias weather=\"python3 {}\"".format(root_dir))
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
    config = open("config.ini", "a")
    parser = configparser.ConfigParser()

    location = input("Enter the location name: ")
    parser.add_section("Config")
    parser.set("Config", "DefaultLocation", location)
    parser.write(config)
    config.close()
