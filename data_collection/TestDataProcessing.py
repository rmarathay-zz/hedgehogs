import pytest
import datetime
from DataProcessing import StockData

"""
This test file test small input to make sure that the
StockData object performs correctly. We can ensure that
the data will be of proper types since it is taken from the
database. So if a data issue occurs, traceback to the data
scraping...
"""

# -----------------------------------------------------------------------------------------------------------------

class TestStockData(object):

    def Accessors_Test(self):
        ticker1 = "TICKER1"
        ticker2 = "TICKER2"
        indicator1 = "close"
        indicator2 = "open"
        data1 = [100, 200, 300]
        dates1 = [datetime.datetime(2019,3,16,0,0),datetime.datetime(2019,3,17,0,0),datetime.datetime(2019,3,18,0,0)]
        data2 = [100, 200, 300, 400]
        dates2 = [datetime.datetime(2019,3,16,0,0),datetime.datetime(2019,3,17,0,0),datetime.datetime(2019,3,18,0,0)]

        sd1 = StockData(ticker1,indicator,dates,data)
        sd2 = StockData(ticker2,indicator,dates,data)
        assert(sd1.getTicker() == "TICKER1")            # Test ticker1
        assert(sd2.getTicker() == "TICKER2")            # Test ticker2
        assert(sd1.getIndicator() == "close")           # Test indicator1
        assert(sd2.getIndicator() == "open")            # Test indicator2
        assert(sd1.getMedian() == 200)                  # Test median1
        assert(sd2.getMedian() == 250)                  # Test median2
        assert(sd1.getMax() == 300)                     # Test max1
        assert(sd2.getMax() == 400)                     # Test max2
        range1 = sd1.getTimeRange()
        range2 = sd2.getTimeRange()
        assert(range1[0] == range2[0] and range1[1] == range2[1])

# -----------------------------------------------------------------------------------------------------------------

    def SimpleMA_Test(self):
        # Test 10 data points for simple moving average, WINDOW=10 & WINDOW=5
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        dates = [datetime.datetime(2019,3,16,0,0),datetime.datetime(2019,3,17,0,0),datetime.datetime(2019,3,18,0,0),
                 datetime.datetime(2019,3,19,0,0),datetime.datetime(2019,3,20,0,0),datetime.datetime(2019,3,21,0,0),
                 datetime.datetime(2019,3,22,0,0),datetime.datetime(2019,3,23,0,0),datetime.datetime(2019,3,24,0,0),
                 datetime.datetime(2019,3,25,0,0)]

        # Test above data
        sd1 = StockData("EX","open",dates,data)
        assert(sd1.simpleMA(1) == [])     # 1-Day window
        assert(sd1.simpleMA(5) == [])     # 5-Day window
        assert(sd1.simpleMA(10) == [])    # 10-Day window

        # Test window out of range
        assert(sd1.simpleMA(15) == [])    # Window out of range

        # Test 1 data point for simple moving average, WINDOW=1
        data = [5]
        dates = [datetime.datetime(2019,3,16,0,0)]
        assert(sd1.simpleMA(1) == [])

# -----------------------------------------------------------------------------------------------------------------

    def ExponentialMA_Test(self):
        # Test 10 data points for exp. moving average, WINDOW=10 & WINDOW=5
        data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        dates = [datetime.datetime(2019,3,16,0,0),datetime.datetime(2019,3,17,0,0),datetime.datetime(2019,3,18,0,0),
                 datetime.datetime(2019,3,19,0,0),datetime.datetime(2019,3,20,0,0),datetime.datetime(2019,3,21,0,0),
                 datetime.datetime(2019,3,22,0,0),datetime.datetime(2019,3,23,0,0),datetime.datetime(2019,3,24,0,0),
                 datetime.datetime(2019,3,25,0,0)]

        # Test above data
        sd1 = StockData("EX","open",dates,data)
        assert(sd1.expMA(1) == [])
        assert(sd1.expMA(5) == [])
        assert(sd1.expMA(10) == [])

        # Test window out of range
        assert(sd1.expMA(15) == [])    # Window out of range

        # Test 1 data point for exp. moving average, WINDOW=1
        data = [5]
        dates = [datetime.datetime(2019,3,16,0,0)]
        assert(sd1.expMA(1) == [])

# -----------------------------------------------------------------------------------------------------------------
