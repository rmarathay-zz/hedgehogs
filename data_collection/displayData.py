import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime

def plotCandleStick(dates, op, cl, hi, lo):
    trace = go.Ohlc(x=dates, open=op, high=hi, low=lo, close=cl)
    data = [trace]
    py.iplot(data, filename='simple_candlestick')


py.tools.set_credentials_file(username='markc373', api_key='MkfbcWDa4kTchHaNmKgI')