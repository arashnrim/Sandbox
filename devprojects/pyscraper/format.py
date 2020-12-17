"""
This file is meant to include all the formats different news sites use for their content. Due to the wide variety of
technologies used by these websites, they differ from one another; for example, the class name of contents can vary
among websites.

Use dictionaries to help organise the formats. Each item in the dictionary should be the domain name of the website.
Each item in the dictionary should be a subdictionary with appropriate values.
"""

formats = {
    "cnn.com": {
        "headline": "Article__title",

        "author_element": "div",
        "author_class": "Article__subtitle",

        # Not required: already in the author element.
        "date_element": "",
        "date_class": "",

        "body_element": "div",
        "body_class": "Paragraph__component"
    },
    "washingtonpost.com": {
        "headline": "font--headline gray-darkest pb-sm null",

        "date_element": "div",
        "date_class": "display-date",

        "author_element": "span",
        "author_class": "author-name font-bold link blue hover-blue-hover",

        "body_element": "p",
        "body_class": "font--body font-copy gray-darkest ma-0 pb-md "
    },
    "reuters.com": {
        "headline": "Headline-headline-2FXIq Headline-black-OogpV ArticleHeader-headline-NlAqj",

        "author_element": "a",
        "author_class": "TextLabel__text-label___3oCVw TextLabel__black-to-orange___23uc0 TextLabel__serif___3lOpX "
                        "Byline-author-2BSir",

        "date_element": "time",
        "date_class": "TextLabel__text-label___3oCVw TextLabel__gray___1V4fk TextLabel__small-all-caps___2Z2RG "
                      "ArticleHeader-date-Goy3y",

        "body_element": "p",
        "body_class": "Paragraph-paragraph-2Bgue ArticleBody-para-TD_9x"
    },
    "nytimes.com": {
        "headline": "css-19rw7kf e1h9rw200",

        "author_element": "span",
        "author_class": "css-1baulvz last-byline",

        "date_element": "time",
        "date_class": "css-129k401 e16638kd0",

        "body_element": "p",
        "body_class": "css-158dogj evys1bk0"
    },
}
