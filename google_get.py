import pandas as pd
import numpy as np
import urlopen
import urllib.request
import datetime as dt
import matplotlib.pyplot as plt
from pandas_datareader import data as web
import datetime as dt
 
def get_google_data(symbol, period, window):
	url_root = 'http://www.google.com/finance/getprices?i='
	url_root += str(period) + '&amp;amp;p=' + str(window)
	url_root += 'd&amp;amp;f=d,o,h,l,c,v&amp;amp;df=cpct&amp;amp;q=' + symbol
	print(url_root)
	request = urllib.request.Request(url_root)
	response = urllib.request.urlopen(request)
	print(response.read())
	data = response.read().split('\n')
	#actual data starts at index = 7
	#first line contains full timestamp,
	#every other line is offset of period from timestamp
	parsed_data = []
	anchor_stamp = ''
	end = len(data)
	for i in range(7, end):
		cdata = data[i].split(',')
	if 'a' in cdata[0]:
	#first one record anchor timestamp
		anchor_stamp = cdata[0].replace('a', '')
		cts = int(anchor_stamp)
	else:
		try:
			coffset = int(cdata[0])
			cts = int(anchor_stamp) + (coffset * period)
			parsed_data.append((dt.datetime.fromtimestamp(float(cts)), float(cdata[1]), float(cdata[2]), float(cdata[3]), float(cdata[4]), float(cdata[5])))
		except:
			pass # for time zone offsets thrown into data
	df = pd.DataFrame(parsed_data)
	df.columns = ['ts', 'o', 'h', 'l', 'c', 'v']
	df.index = df.ts
	del df['ts']
	return df
data = pd.read_csv("https://s3.amazonaws.com/static.quandl.com/tickers/nasdaq100.csv")
 
start = dt.datetime(2016, 3, 7)
end = dt.datetime(2017, 3, 7)
 
volume = []
closes = []
good_tickers = []
for ticker in data['ticker'].values.tolist():
	print (ticker)
	vdata = get_google_data(ticker, 60, 10)
	print("SSS")
	cdata = vdata[['c']]
	closes.append(cdata)
	vdata = vdata[['v']]
	volume.append(vdata)
	good_tickers.append(ticker)
	print("x")
print("HII :",volume)
#closes = pd.concat(closes, axis = 1)
#closes.columns = good_tickers
 
#diffs = np.log(closes).diff().dropna(axis = 0, how = "all").dropna(axis = 1, how = "any")
#diffs.head()
#print(diffs)




