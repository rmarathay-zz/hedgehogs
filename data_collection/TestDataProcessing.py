import pytest
from DataProcessing import StockData

"""
IMPLEMENT A TEST FILE TO TEST THE FUNCTIONS
IN DataProcessing.py this should develop
fake data and and ensure that the calculations
are correct and that the data types are correct
"""

def SetUp():
    # Single entry data set
    ticker2 = "TIC2"
    dat2 = []
    ts2 = []

    # Small data set
    ticker3 = "TIC3"
    dat3 = []
    ts3 = []

    # Slightly larger data set
    ticker4 = "TIC4"
    dat4 = []
    ts4 = []

    # Invalid prices
    ticker5 = "TIC5"
    dat5 = [1, "one", 1.0]
    ts4 = []

    # Invalid timestamps
    ticker6 = "TIC6"
    dat6 = [1.0, 2.0, 3.0]
    ts4 = ["one", 2, 3.0]


class TestStockData(object):

    def Constructor_Test(self):

        prices = []
        dates = []
        badPrices = []
        badDates = []

        sd1 = StockData("AAPL","open",[],[])           # Empty data lists
        sd2 = StockData(5,"open",dates,prices)         # Invalid ticker
        sd3 = StockData("AAPL",5,dates,prices)         # Invalid indicator
        sd4 = StockData("AAPL","open",dates,badPrices) # Invalid prices
        sd5 = StockData("AAPL","open",badDates,prices) # Invalid timestamps

    def Accessors_Test(self):

        prices = []
        dates = []

        sd1 = StockData("AAPL","open",dates,prices)
        sd2 = StockData("AAPL","open",dates,prices)

    def InvalidTypes_Test(self):
        return

    def SimpleMA_Test(self):
        return

    def ExponentialMA_Test(self):
        return
