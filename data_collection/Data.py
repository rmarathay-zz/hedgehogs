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
