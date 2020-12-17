import sys
import requests
from bs4 import BeautifulSoup

try:
    LINK = sys.argv[1]
except IndexError:
    sys.exit("No URL was given in the program argument; try again.")

REQUEST = requests.get(LINK)
TEXT = REQUEST.text

if "cnn.com" in LINK:
    ELEMENT = "span"
else:
    ELEMENT = "p"

for paragraph in BeautifulSoup(TEXT, features="html.parser").find_all(ELEMENT):
    print(paragraph.get_text())
