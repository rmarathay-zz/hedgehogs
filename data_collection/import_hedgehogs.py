# HEDGEHOGS IMPORT FILE
#   CONTAINS ALL MODULES AND CLASSES


from lxml import html
from bs4 import BeautifulSoup
import urllib
import pycurl
from StringIO import StringIO
from pymongo import MongoClient
import datetime
import pprint

class Data():
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.data = {}

    def getUrl(self):
        return self.url

    def getName(self):
        return self.name

    def addItem(self, key, value):
        self.data[key] = value

    def printItems(self):
        for item in self.data:
            print item, self.data[item]

    def printKeys(self):
        for k in self.data.keys():
            print k

    def getKeys(self):
        keys = [ ]
        for k in self.data.keys():
            keys.append(k)
        return keys

    def getValue(self,key):
        print self.data[key]

    def getData(self):
        return self.data

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
