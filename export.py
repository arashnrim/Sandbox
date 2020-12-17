"""
This file performs all the code to export the text scraped from the articles into a file.
"""
import os


def export(content):
    headline = content["headline"]
    author = content["author"]
    try:
        date = content["date"]
    except KeyError:
        pass
    body = content["body"]

    if not os.path.exists("{}/articles".format(os.path.dirname(os.path.abspath(__file__)))):
        os.mkdir("articles")

    with open("articles/{}".format(headline), "w") as file:
        file.write(headline + "\n")
        file.write(author + "\n")
        try:
            file.write(date + "\n")
        except NameError:
            pass
        file.write("\n")
        for index, paragraph in enumerate(body):
            if index != len(body) - 1:
                file.write(paragraph + "\n")
            else:
                file.write(paragraph)
