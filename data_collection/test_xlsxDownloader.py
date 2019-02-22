# To get tests and time (good to find slow tests)
# pytest --durations=0
# replace 0 with positive integers to get x slowest tests (with times)

from xlsxDownloader import *
import pytest
import requests
import os.path

tickers = ["TSLA", "AAPL", "GOOG", "AMZN", "NFLX"]

def test_linksValid():
	template = "https://www.sec.gov"
	for count in range(len(tickers)):
		top_level_links = createTopLevelURLs(tickers[count])
		for i in range(len(top_level_links)):
			connect = requests.get(template+top_level_links[i])
			assert connect.status_code == 200, "Invalid url is " + template + connect

def test_ParseURL():
	xlsx_links = createParseableUrls(createTopLevelURLs("TSLA"))
	for i in range(len(xlsx_links)):
		connect = requests.get(xlsx_links[i])
		assert connect.status_code == 200, "Invalid url is " + connect

def test_downloadXlxs():
	root_folder = 'fin_data'
	for count in range(len(tickers)):
		downloadXlxs(createParseableUrls(createTopLevelURLs(tickers[count])), tickers[count])
		os.chdir('..')
		assert os.path.exists(tickers[count]), "Folder for ticker " + tickers[count] + " at path " + file_path + " not found"
		os.chdir(tickers[count])	
		assert len(os.listdir()) > 0, "No files created for ticker " + tickers[count]
		os.chdir('../../')
