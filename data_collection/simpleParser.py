import re

def getAVantageKeys():
"""

parses credentials.json and allows other program files to access API keys to scrape data

Returns:
	list of size 2 containing two API keys to use for scraping data

"""           
	AVantageKeys = []                																																										
	f = open("credentials.json", 'r')
	contents = f.read().split('\n')
	unparsed = [item for item in contents if item.startswith('scraperAPI')]
	for element in unparsed:
		AVantageKeys.append(re.findall(r'"([^"]*)"', element)[0].strip("[]"))
	return AVantageKeys

def getPasswordDB():
"""

parses credentials.json and allows other program files to access database password for user 'rcos' to create tables/schemas

Returns:
	list of size 1 containing password for user 'rcos' in database

"""
	PasswordDB = []
	f = open("credentials.json", 'r')
	contents = f.read().split('\n')
	unparsed = [item for item in contents if item.startswith('PasswordDB')]
	for element in unparsed:
		PasswordDB.append(re.findall(r'"([^"]*)"', element)[0].strip("[]"))
	return PasswordDB
