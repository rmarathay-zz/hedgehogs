import re

def getAVantageKeys():           
	AVantageKeys = []                																																										
	f = open("credentials.json", 'r')
	contents = f.read().split('\n')
	unparsed = [item for item in contents if item.startswith('scraperAPI')]
	for element in unparsed:
		AVantageKeys.append(re.findall(r'"([^"]*)"', element)[0].strip("[]"))
	return AVantageKeys

def getPasswordDB():
	PasswordDB = []
	f = open("credentials.json", 'r')
	contents = f.read().split('\n')
	unparsed = [item for item in contents if item.startswith('PasswordDB')]
	for element in unparsed:
		PasswordDB.append(re.findall(r'"([^"]*)"', element)[0].strip("[]"))
	return PasswordDB
