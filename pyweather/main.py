from art import tprint

from onboarding import *

# Tries to read if the user has set up the program before.
# Otherwise, the user is directed to on-boarding.
try:
    config = open("config.ini", "r")
except OSError:
    configured = False
else:
    configured = True

print("==========================")
tprint("pyweather")
print("==========================", end="\n\n")

sleep(2)
if not configured:
    welcome()
