from lxml import html
from bs4 import BeautifulSoup
import urllib
import pycurl
from StringIO import StringIO
from pymongo import MongoClient
import datetime
import pprint


class Link():
    def __init__(self, name, link):
        self.name = name
        self.link = link

    def getUrl(self):
        return self.link

    def getName(self):
        return self.name

    def getHTML(self):
        buffer = StringIO()
        c = pycurl.Curl()
        c.setopt(c.URL, self.getUrl())
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        body = buffer.getvalue()
        return body
