from time import sleep
import os
from pathlib import Path
import configparser

"""
Welcomes the user to the project and guides them through onboarding.
"""
def welcome():
    print("Welcome to pyweather, a command-line weather tool to get information about the weather right from your terminal.", end="\n\n")
    sleep(2)
    while True:
        print("Would you like to save pyweather to your rc file? This allows you to run 'weather' at any time in your terminal.", end=" ")
        save = input("(y/n): ")
        if save == "y" or save == "Y":
            saveInPathCompletion(saveInPath())
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
            saveDefault()
            break
        elif save == "n" or save == "N":
            break
        else:
            print("Invalid. Set a default location?", end=" ")
    sleep(2)
    print()
    print("That's it. Thanks for setting up!")

def saveInPath():
    shell = os.environ['SHELL']
    if shell == "/bin/zsh":
        profile = "{}/.zshrc".format(Path.home())
    elif shell == "/bin/bash":
        profile = "{}/.bashrc".format(Path.home())

    try:
        rc = open(profile, "a")
        root_dir = os.path.dirname(os.path.abspath(__file__))
        rc.write("\"alias weather=python3 {}\"".format(root_dir))
        rc.close()
    except:
        return False
    else:
        return True

def saveInPathCompletion(status):
    if status:
        print("Operation successful!", end="\n\n")
    else:
        print("Something went wrong. Please try again later.", end="\n\n")

def saveDefault():
    config = open("config.ini", "a")
    parser = configparser.ConfigParser()

    location = input("Enter the location name: ")
    parser.add_section("Config")
    parser.set("Config", "DefaultLocation", location)
    parser.write(config)
    config.close()
