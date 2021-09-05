import sys

import requests
from bs4 import BeautifulSoup

from format import formats
from export import export

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
        HEADLINE = BeautifulSoup(TEXT, features="html.parser").find_all("h1", {"class": headline_class})[0].get_text()
        print("\033[1m{}\033[0m".format(HEADLINE))

        # Gets the author of the article.
        AUTHOR = BeautifulSoup(TEXT, features="html.parser").find_all(author_element, {"class": author_class})[
            0].get_text()
        print(AUTHOR)

        # Gets the date of the article.
        if date_element and date_class:
            DATE = BeautifulSoup(TEXT, features="html.parser").find_all(date_element, {"class": date_class})[
                0].get_text()
            print(DATE)

print()

# Gets the main content of the article.
BODY = []
for element in BeautifulSoup(TEXT, features="html.parser").find_all(BODY_ELEMENT, {"class": BODY_CLASS}):
    print(element.get_text())
    BODY.append(element.get_text())

# Exports the article into a file.
try:
    export({
        "headline": HEADLINE,
        "author": AUTHOR,
        "date": DATE,
        "body": BODY
    })
except NameError:
    export({
        "headline": HEADLINE,
        "author": AUTHOR,
        "body": BODY
    })
