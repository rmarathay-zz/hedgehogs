# HEDGEHOGS IMPORT FILE
#   CONTAINS ALL MODULES AND CLASSES


##from lxml import html
##from lxml import etree
##from optparse import OptionParser
##from openpyxl import load_workbook
from bs4 import BeautifulSoup
from io import StringIO
from pymongo import MongoClient
from collections import OrderedDict as OD
from optparse import OptionParser
from pymongo import MongoClient, bulk
from bson import json_util
import collections
import io
import urllib
##import pycurl
import html2text
import sys
import os
import wget
import xlrd
import pandas
import datetime
import pprint
import string
import re
import json
import openpyxl
import csv


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
            print(item, self.data[item])

    def printKeys(self):
        for k in self.data.keys():
            print(k)

    def getKeys(self):
        keys = [ ]
        for k in self.data.keys():
            keys.append(k)
        return keys

    def getValue(self,key):
        print(self.data[key])

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
        fp = urllib.request.urlopen(self.getUrl())
        _bytes = fp.read()
        _str = _bytes.decode("utf8")
        return _str
#         buffer = StringIO()
#         c = pycurl.Curl()
#         c.setopt(c.URL, self.getUrl())
#         c.setopt(c.WRITEDATA, buffer)
#         c.perform()
#         c.close()
#         body = buffer.getvalue()
#        return body
class MongoConnection():
    def __init__(self, username, password):
        self.MONGO_HOST = "45.55.48.43"
        self.MONGO_PORT = 27107
        self.MONGO_DB0 = "admin"
        self.MONGO_DB1 = "SEC_EDGAR"
        self.MONGO_USER = username
        self.MONGO_PASS = password
    def connect(self):
        client = MongoClient(MONGO_HOST, MONGO_PORT, username=MONGO_USER, password=MONGO_PASS, authMechanism='SCRAM-SHA-1')
        db = client[MONGO_DB1]
