# v0.0.2

from lxml import html
from lxml import etree
from bs4 import BeautifulSoup
#from StringIO import StringIO
from io import StringIO
from optparse import OptionParser
from pymongo import MongoClient
from html.parser import HTMLParser
from openpyxl import load_workbook
import urllib
from urllib.request import urlopen
import datetime
import pprint
import html2text
import sys, os
import wget
import pandas
import xlrd

from import_hedgehogs import Link
from import_hedgehogs import Data

def createTopLevelURLs(ticker):
    top_level_links = []
    top_level_link = "https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=" + ticker + "&type=10-Q&dateb=&owner=exclude&count=4"
    tl_link = Link('top_level_link', top_level_link)
    pre_soup = tl_link.getHTML()
    soup = BeautifulSoup(pre_soup, 'lxml')
    print("Creating Top Level URLs...")
    for doc in soup.find_all('a', attrs={'id' : 'interactiveDataBtn'}):
        top_level_links.append(str(doc['href']))
    return top_level_links

def createParseableUrls(top_level_links):
    header_link = "https://www.sec.gov"
    return_list = []
    print("Creating Parseable URLs...")
    for link in top_level_links:
        q10_link = Link('link', header_link + link)
        pre_soup = q10_link.getHTML()
        soup = BeautifulSoup(pre_soup, 'lxml')
        for xlxs in soup.find_all('a', attrs={'class' : 'xbrlviewer'}):
            if(xlxs.contents[0] == 'View Excel Document'):
                return_list.append(header_link + str(xlxs['href']))
        return return_list

def downloadXlxs(xlxs_links, ticker):
    print("Downloading .xlxs files...")
    os.chdir('fin_data')
    os.mkdir(ticker)
    os.chdir(ticker)
    for i in range(0,len(xlxs_links)):
        filename = wget.download(xlxs_links[i], str(i)+".xlsx")
        #filename = wget.download(xlxs_links[i],"")
        print("AHHH")
        #filename = filename.replace("Financial_Report",str(i))
        print("This is",filename)
        
    for i in os.listdir('.'):
        excelFile = pandas.ExcelFile(i)
        #print(excelFile)
        print(pandas.ExcelFile(i))
        sheetNames = excelFile.sheet_names
        for sheet in sheetNames:
            print('\n')
            print("This s1")
            print(sheet)
            sheet = excelFile.parse(sheet)
            print("This s2")
            print(sheet)
            print('\n')
            break
        break

def initializer():
    cli_parser = OptionParser(
        usage='usage: %prog <input.xlsx> [output.json]'
    )
    (options, args) = cli_parser.parse_args()
    # Input file checks
    if len(args) < 1:
        cli_parser.error("You have to supply at least 1 argument")
        print("Version 2.0.1")
    client = MongoClient('localhost', 12345)
    if(client):
        print("Connected to MonogClient: localhost port 12345")
    ticker = sys.argv[1]
    topLevelLinks = createTopLevelURLs(ticker)
    parseLinks = createParseableUrls(topLevelLinks)
    downloadXlxs(parseLinks, ticker)

if __name__ == '__main__':
    initializer()
