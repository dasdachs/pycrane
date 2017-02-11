#! /usr/bin/env python3
"""
A simple law parser in Python
"""
__author__ = "Jani Šumak"
__version__ = "0.1"
import re


# Python2 ARTICLE_TOKEN = re.compile(r"\d\.\s\w+(?=\n)", re.UNICODE)
ARTICLE_TOKEN = re.compile(r"\d\.\s\w+(?=\n)")
PARAGRAPH_TOKEN = re.compile(r"")


class Article(object):
    """
    An Article is the main element of any bill or contract. It 
    """
    def __init__(self, article_number, paragraphs, title=None):
        """
        An article is divided into paragraphs. Paragraphs are
        represented by a Paragraph object.

        :param article_number: the article number (string)
        :param paragraphs: a tuple of Paragraphs (tuple)
        :param title: a special paragraph, usually the first (string)
         after the article num
        """
        self.article_number = article_number
        self.title = title
        self.paragraphs = paragraphs
   
   @property
   def text(self):
       paragraphs = [para.text for para in self.paragraphs]
       article_text = "".join(paragraphs)
       return article_text

   def __str__(self):
       return self.title if self.title else self.article_number

   def __repr__(self):
       return "Article <%s>" % self.article_number 


def parse_text(text=None, file=None):
    """
    Parses a string, an StringIO object or opens a file.
    """
    if not text:
        text = open(file).readlines()
    parsed_text = re.split(ARTICLE_TOKEN, text)
    return parsed_text
tmp = t[:]
    ...: for x in re.findall(, t):
            ...:     found = tmp[:tmp.find(x)]
                ...:     print(found)
                    ...:     tmp = tmp.split(found)[1]
                        ...:     print(10*"=")
                            ...: print(tmp)
