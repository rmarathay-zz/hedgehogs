'''
COMMAND LINE ARGUMENTS

tics.txt start_date end_date ticker

date format is year-month-date

'''
import plotly.plotly as py
#import plotly as py
from plotly.tools  import FigureFactory as FF
from datetime import datetime
from datetime import date
import pandas as pd
import sys
import plotly.graph_objs as go
import fetch_stocks
dic = {}
open_data = []
dates = []
fetch_stocks.get_candleData(sys.argv[1],sys.argv[2],sys.argv[3],['Open', 'High', 'Low', 'Close', 'Volume'])
f = open("stocks_csv/Open.csv")
line =f.readline().strip().split(",")
print(line)
ticker_index = line.index(sys.argv[4])
print(ticker_index)
for line in f:
	line = line.strip().split(",")
	temp_date=line[0].split("-")
	dates.append(datetime(year = int(temp_date[0]) , month = int(temp_date[1]) , day =int(temp_date[2])))
	open_data.append(line[ticker_index])
f.close()
dic["Open"] = open_data
dic["Dates"] = dates

close_data = []
f = open("stocks_csv/Close.csv")
line =f.readline().strip().split(",")
for line in f:
	line = line.strip().split(",")
	close_data.append(line[ticker_index])

dic["Close"] = close_data
high_data = []
f = open("stocks_csv/High.csv")
line =f.readline().strip().split(",")
for line in f:
	line = line.strip().split(",")
	high_data.append(line[ticker_index])
dic["High"] = high_data
low_data = []
f = open("stocks_csv/Low.csv")
line =f.readline().strip().split(",")
for line in f:
	line = line.strip().split(",")
	low_data.append(line[ticker_index])
dic["Low"] =low_data
df = pd.DataFrame(data = dic)
print(df)
#py.sign_in('ml.hawks12', '30Jeb05NUXNrgxUMSqTK')
trace = go.Candlestick(x=df.Dates,
                       open=df.Open,
                       high=df.High,
                       low=df.Low,
                       close=df.Close)
#print(type(trace))

data = [trace]
#print(data)
py.iplot(data, filename='simple_candlestick')
#x=py.offline.plot(data, include_plotlyjs = False, output_type = 'div')
#print(x)