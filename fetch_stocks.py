'''from pandas_datareader import data as pdr

import fix_yahoo_finance as yf
yf.pdr_override() # <== that's all it takes :-)

# download dataframe
data = pdr.get_data_yahoo("SPY", start="2017-01-01", end="2017-04-30")

# download Panel
data = pdr.get_data_yahoo(["SPY", "IWM"], start="2017-01-01", end="2017-04-30")
print(data)
'''
from pandas_datareader import data
import pandas as pd
import json
import fix_yahoo_finance as yf
import sys
import plotly.plotly as py
import plotly.graph_objs as go


#30Jeb05NUXNrgxUMSqTK
# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
def get_candleData(filename, start_date, end_date, keys):
	# Dates should be in the format of "year-month-day"
	for key in keys:
		tickers_enter = []
		f = open(filename)
		for tic in f:
			print(tic)
			tickers_enter.append(tic.strip())
		#tickers_enter = ['AAPL','MSFT']#, 'MSFT']#, 'SPY']
		yf.pdr_override()
		# Define which online source one should use
		data_source = 'yahoo'

	
		# User pandas_reader.data.DataReader to load the desired data. As simple as that.
		#panel_data = data.get_data_yahoo(tickers, start_date, end_date)
		panel_data = data.get_data_yahoo(
				tickers = tickers_enter,
				start = start_date,
				end = end_date
		)
		print(list(panel_data))
		something = panel_data.ix[key] #['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
		# Getting all weekdays between 01/01/2000 and 12/31/2016
		hourly_dates = pd.date_range(start_date, end_date, freq='D')
		something = something.reindex(hourly_dates)

		print(something)

		something = something.fillna(method='ffill')
		#panel_data.to_excel("/Users/mike/Desktop/hedgehogs/test_stocks2.xlsx")
		path = "/Users/mike/Desktop/hedgehogs/stocks_csv/" + key + ".csv"
		ls=something.to_csv(path)
		f = open(path,'r+')
		lines = f.readlines() # read old content
		f.seek(0) # go back to the beginning of the file
		f.write("Date") # write new content at the beginning
		for line in lines: # write old content after new
		    f.write(line)
		f.close()

get_candleData("tics.txt", "2013-3-2","2016-3-4",['Open', 'High', 'Low', 'Close', 'Volume'])
#print(ls)

#something = something.fillna(method = 'ffill')
#x = something.head(7)
#print(type(panel_data))
#something.to_excel("/Users/mike/Desktop/hedgehogs/test_stocks.xlsx")