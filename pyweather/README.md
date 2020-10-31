# 🔆 pyweather

## Table of Contents
- [Introduction](#introduction)
- [About the project](#about-the-project)
- [Using the project](#using-the-project)
- [Tools used](#tools-used)
- [Learning log](#learning-log)

## Introduction
Welcome to pyweather! This is meant to be an experimental and learning project for me. 

Here are my main takeaways from this project:

- **Interacting with APIs** — through this project, I managed to learn more about how to interact with different APIs. I learned that most return in the form of JSON, and I needed to use Python's `json` to read requests.
- **Using `urllib`** — through this project, I learned to use the `urllub` library to handle requests. I learned more about different response codes, including 200 (OK), 404 (Not Found), and 429 (Too Many Requests).
- **Handling local directories** — through this project, I learned how to handle navigating through local directories. In most cases, I found `os` and/or `sys` to be really helpful on this end.
- **Reading from `.ini` files** — through this project, I learned how to read and write to `.ini` files with the help of the `configparser` module.

## About the project
This project is made with **Python**.

The app has one main purpose: retrieve weather information for a given city and display it nicely in the terminal. It'll be nice to have it as a tool readily-available!

## Using the project
These instructions assume that you have Python 3 installed. If not, visit [the website](https://python.org) to grab a version of Python. This project was created with Python 3.6.8.

1. Head over to the [OpenWeatherMap](https://openweathermap.org) website and create an account to gain an API key.
2. Clone the project and save it somewhere accessible.
3. Using a terminal, navigate to the project.
4. Run `pip3 install -r requirements.txt`.
5. Run `python3 main.py`.
6. The program should run and guide you through on-boarding. It's essential to store your API key here.

## Tools used
Through this project, I was introduced to a lot of tools — both that helped with code directly or indirectly. Here's a list of the tools I've used for this project:

- [Art](https://pypi.org/project/art/) — cool module for neat ASCII text art!
- [OpenWeatherMap API](https://openweathermap.org/api) — main API source for weather information
- [PyCharm CE](https://www.jetbrains.com/pycharm/) — an open-source and handy IDE for Python development.

## Learning log
- [Working With JSON Data in Python](https://realpython.com/python-json/)
- [Python - Get path of root project structure](https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure)
- [How to get the home directory in Python?](https://stackoverflow.com/questions/4028904/how-to-get-the-home-directory-in-python)
- [Current weather data](https://openweathermap.org/current)
- [`configparser` — Configuration file parser](https://docs.python.org/3/library/configparser.html)
- [Programmatically stop execution of python script?](https://stackoverflow.com/questions/543309/programmatically-stop-execution-of-python-script)
- [Proper way to declare custom exceptions in modern Python?](https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python)
- [string capitalize() in Python](https://www.geeksforgeeks.org/string-capitalize-python/)
- [How do I print bold text in Python?](https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python)