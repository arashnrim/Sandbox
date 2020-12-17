# pyscraper

## Table of Contents
- [Introduction](#introduction)
- [About the project](#about-the-project)
- [Using the project](#using-the-project)
- [Tools used](#tools-used)
- [Learning log](#learning-log)

## Introduction
Welcome to pyscraper! This is meant to be an experimental and learning project for me. This project was created specially for a practice assignment at [DevProjects](https://www.codementor.io/projects/web-scraper-to-get-news-article-content-atx32d46qe).

This project took approximately two hours to make. 

Here are my main takeaways from this project:
- **Web scraping** — through this project, I learnt how to use the [Requests](https://requests.readthedocs.io/en/master/) and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) modules to scrape text off news articles.

## About the project
This project is made with **Python**.

The program simply scrapes the byline, author name, updated date, and main body of a news articles and displays it to the user. The program also saves this scraped content into a file.

## Using the project
These instructions assume that you have Python 3 installed and you are using `bash` or `zsh`. If not, visit [the website](https://python.org) to grab a version of Python. This project was created with Python 3.6.8.

1. Clone the project and save it somewhere accessible.
2. Using a terminal, navigate to the project.
3. In the pyscraper directory, run `source bin/activate`.
    - If you are not using `bash` or `zsh`, refer to [this table](https://docs.python.org/3/library/venv.html) for which file to run.
4. Run `python3 scraper.py <link>`, where `<link>` is a link to an article.
5. The program should run and scrape the data from this source.

> **Note:** Currently, only the following websites are supported:
> - [The New York Times](https://www.nytimes.com/)
> - [CNN](https://edition.cnn.com/)
> - [The Washington Post](https://www.washingtonpost.com/)
> - [Reuters](https://www.reuters.com/) 

## Tools used
Through this project, I was introduced to a lot of tools — both that helped with code directly or indirectly. Here's a list of the tools I've used for this project:

- [Requests](https://requests.readthedocs.io/en/master/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
- [DevProjects](https://www.codementor.io/projects)

## Learning log
- [Requests documentation](https://requests.readthedocs.io/en/master/)
- [Beautiful Soup documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
