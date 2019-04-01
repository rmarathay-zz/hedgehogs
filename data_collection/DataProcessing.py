from statistics import median
import matplotlib.pyplot as plt
import numpy as np
from numpy import convolve


class StockData:

    def __init__(self, ticker, column_type, column_dates, column_data):
        """

        constructor to create StockData object

        Arguments:
            self.ticker: stores the ticker
            self.indicator: stores the indicator
            self.data: list of tuple holing timestamp and price in
            self.prices: numpy array of only prices

        """
        self.ticker = ticker
        self.indicator = column_type
        self.data = []
        self.prices = np.array(column_data)
        for price, date in zip(column_data, column_dates):
            self.data.append( (date, price) )
            np.append(self.prices, np.asarray(price))


    def getTicker(self):
        """

        method to get ticker for object
        
        Returns:
            the ticker i.e. 'MSFT'
        
        """
        return self.ticker


    def getIndicator(self):
        """
        
        method to get indicator for object

        Returns:
             the indicator i.e. 'open' OR 'high'

        """
        return self.indicator


    def getMax(self):
        """
        
        returns the maximum price for the stock

        Returns:
            a float containing the max price
        

        """
        return max(self.prices)


    def getMedian(self):
        """
        
        returns the median price for the stock

        Returns:
            a float containing the median price
        

        """
        return median(self.prices)


    def getTimeRange(self):
        """
        
        returns a tupe containing the start date and end date

        Returns:
            a tuple containing the start timestamp and the ending time stamp.
        

        """
        return (self.data[0][0], self.data[-1][0])


    def simpleMA(self, window):
        """
        
        calculates moving average for the given window

        Arguments:
            window: a number of days for each avg value

        Raises:
            ValueError: if window parameter was not integer

        Returns:
            the moving average


        """
        # Calculates a simple moving average over the window given.
        # @params: window, a number of days for each avg value
        if (window > len(self.prices)):
            return
        try:
            sma = np.cumsum(self.prices, dtype=float)
            sma[window:] = sma[window:] - sma[:-window]
            return sma[window-1:] / window
        except ValueError:
            print("Window value needs to be an integer.")


    def expMA(self, window):
        """

        calculates an exponential moving average by adding a weight to the last 'window' days.

        Arguments:
            window: a number of days for each avg value (default value 10)

        Returns:
            an np array holding MA values computed with exp.
        """
        if (window > len(self.prices)):
            window = 10
        if (window <= 0):
            window = 10
        alpha = np.float64(2.0 / (window + 1.0))
        alpha_rev = np.float64(1-alpha)
        n = self.prices.shape[0]             # n = number of array rows

        pows = alpha_rev ** (np.arange(n+1)) # Build exponents array
        scale_vector = 1 / pows[:-1]
        offset = self.prices.data[0]*pows[1:]
        pw0 = alpha * alpha_rev**(n-1)

        mult = self.prices.data * pw0 * scale_vector
        cum_sums = mult.cumsum()
        out_vec = offset + cum_sums*scale_vector[::-1]
        return out_vec


    def printData(start, end):
        """
        
        prints the ticker and the indicator held within self

        Arguments:
            start: start date to print data
            end: end date to print data


        """
        length = len(self.data)
        if (start > length and end > length):
            print("Invalid range entered!")
            return

        if (start < 0):    # Start must be >= 0
            start = 0
        if (end > length): # End must be <= len(self.data)
            end = length
        if (start > end):  # Swap if start > end
            start, end = end, start
        print( "TICKER:\t {}".format(self.ticker) )
        print( "INDICATOR:\t {}\n".format(self.indicator) )
        counter = 0
        for i in range(start, end):
            if (counter % 8 == 0):
                print("")
            print(self.data[i])
            counter += 1
