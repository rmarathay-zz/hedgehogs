import datetime
from DataProcessing import StockData

# -----------------------------------------------------------------------------------------------------------------

def Accessors_Test():
    ticker1 = "TICKER1"
    ticker2 = "TICKER2"
    indicator1 = "close"
    indicator2 = "open"
    data1 = [100, 200, 300]
    dates1 = [datetime.datetime(2019,3,16,0,0),datetime.datetime(2019,3,17,0,0),datetime.datetime(2019,3,18,0,0)]
    data2 = [100, 200, 300, 400]
    dates2 = [datetime.datetime(2019,3,16,0,0),datetime.datetime(2019,3,17,0,0),datetime.datetime(2019,3,18,0,0)]

    sd1 = StockData(ticker1,indicator1,dates1,data1)
    sd2 = StockData(ticker2,indicator2,dates2,data2)
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

def SimpleMA_Test():
    # Test 10 data points for simple moving average, WINDOW=10 & WINDOW=5
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dates = [datetime.datetime(2019,3,16,0,0),datetime.datetime(2019,3,17,0,0),datetime.datetime(2019,3,18,0,0),
             datetime.datetime(2019,3,19,0,0),datetime.datetime(2019,3,20,0,0),datetime.datetime(2019,3,21,0,0),
             datetime.datetime(2019,3,22,0,0),datetime.datetime(2019,3,23,0,0),datetime.datetime(2019,3,24,0,0),
             datetime.datetime(2019,3,25,0,0)]
    sd = StockData("APPL","open",dates,data)
    print("Data Set:                ", data)
    print("WINDOW=5  Simple MA Data:", sd.simpleMA(5))
    print("Data Set:                ", data)
    print("WINDOW=10 Simple MA Data:", sd.simpleMA(10))
    print("")

    # Test 1 data point for simple moving average, WINDOW=1
    data = [5]
    dates = [datetime.datetime(2019,3,16,0,0)]
    sd = StockData("APPL","open",dates,data)
    print("Data Set:                ", data)
    print("WINDOW=1 Simple MA Data: ", sd.simpleMA(1))
    print("")

    # Test window out of range
    data = [5, 10, 15]
    dates = [datetime.datetime(2019,3,16,0,0),datetime.datetime(2019,3,17,0,0),datetime.datetime(2019,3,18,0,0)]
    sd = StockData("APPL","open",dates,data)
    print("Data Set:                ", data)
    print("WINDOW=5 Simple MA Data: ", sd.simpleMA(5))

# -----------------------------------------------------------------------------------------------------------------

def ExponentialMA_Test():
    # Test 10 data points for exp. moving average, WINDOW=10 & WINDOW=5
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    dates = [datetime.datetime(2019,3,16,0,0),datetime.datetime(2019,3,17,0,0),datetime.datetime(2019,3,18,0,0),
             datetime.datetime(2019,3,19,0,0),datetime.datetime(2019,3,20,0,0),datetime.datetime(2019,3,21,0,0),
             datetime.datetime(2019,3,22,0,0),datetime.datetime(2019,3,23,0,0),datetime.datetime(2019,3,24,0,0),
             datetime.datetime(2019,3,25,0,0)]
    sd = StockData("MSFT","open",dates,data)
    print("Data Set:              ", data)
    print("WINDOW=10 Exp Data Set:", sd.simpleMA(10))
    print("WINDOW=5  Exp Data Set:", sd.simpleMA(5))

    # Test 1 data point for exp. moving average, WINDOW=1
    data = [5]
    dates = [datetime.datetime(2019,3,16,0,0)]
    sd = StockData("MSFT","open",dates,data)
    print("Data Set:              ", data)
    print("WINDOW=1 Exp Data Set: ", sd.expMA(1))

    # Test window out of range
    data = [5, 10, 15]
    dates = [datetime.datetime(2019,3,16,0,0),datetime.datetime(2019,3,17,0,0),datetime.datetime(2019,3,18,0,0)]
    sd = StockData("MSFT","open",dates,data)
    print("Data Set:               ", data)
    try:
        print("WINDOW=5 ExpMA Data Set:", sd.expMA(5))
    catch (ValueError e):
        print("Caught an exception for an invalid range. Should be |3|, was |5|")

# -----------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    print("Beginning a test for StockData accessor methods...")
    Accessors_Test()
    print("\tALL TESTS PASSED!\n")
    print("Beginning a test for Simple MA and Exponential MA...\n")
    print("=========================== SIMPLE MA TEST ==========================\n")
    SimpleMA_Test()
    print("\n=========================== EXP MA TEST ===========================\n")
    ExponentialMA_Test()
    print("\tALL TESTS PASSED!")
