import sys

import requests
from bs4 import BeautifulSoup

from format import formats

try:
    LINK = sys.argv[1]
except IndexError:
    sys.exit("No URL was given in the program argument; try again.")

REQUEST = requests.get(LINK)
TEXT = REQUEST.text

for link in formats:
    if link in LINK:
        BODY_ELEMENT = formats[link]["body_element"]
        BODY_CLASS = formats[link]["body_class"]
        headline_class = formats[link]["headline"]
        author_element = formats[link]["author_element"]
        author_class = formats[link]["author_class"]
        date_element = formats[link]["date_element"]
        date_class = formats[link]["date_class"]

        # Gets the headline of the article.
        headline = BeautifulSoup(TEXT, features="html.parser").find_all("h1", {"class": headline_class})[0].get_text()
        print("\033[1m{}\033[0m".format(headline))

        # Gets the author of the article.
        author = BeautifulSoup(TEXT, features="html.parser").find_all(author_element, {"class": author_class})[
            0].get_text()
        print(author)

        # Gets the date of the article.
        if date_element and date_class:
            date = BeautifulSoup(TEXT, features="html.parser").find_all(date_element, {"class": date_class})[
                0].get_text()
            print(date)

print()

# Gets the main content of the article.
for element in BeautifulSoup(TEXT, features="html.parser").find_all(BODY_ELEMENT, {"class": BODY_CLASS}):
    print(element.get_text())
