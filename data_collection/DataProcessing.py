import matplotlib.pyplot as plt
import numpy as np
from numpy import convolve


class StockData:


    def __init__(self, ticker, column_type, column_dates, column_data):
        # Expects that column dates correspond with the proper column data
        # Stores the ticker, indicator, a separate np_array of prices
        # for quicker processing, and a list of tuples containing the
        # time stamp and price.
        self.ticker = ticker
        self.indicator = column_type
        self.data = []
        self.prices = np.array(column_data)
        for price, date in zip(column_data, column_dates):
            self.data.append( (date, price) )
            np.append(self.prices, np.asarray(price))


    def getTicker(self):
        # Returns the ticker i.e. 'MSFT'
        return self.ticker


    def getIndicator(self):
        # Returns the indicator i.e. 'open' OR 'high'
        return self.indicator


    def simpleMA(self, window):
        # Calculates a simple moving average over the window given.
        # @params: window, a number of days for each avg value
        try:
            sma = np.cumsum(self.prices, dtype=float)
            sma[window:] = sma[window:] - sma[:-window]
            return sma[window-1:] / window
        except ValueError:
            print("Window value needs to be an integer.")


    def expMA(self, window):
        # Calculates an exponential moving average over the window given
        # @params: window, a number of days for each avg value
        # @returns:
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
        # @params: Range of values to print
        # Prints the ticker and the indicator held within self
        # Prints rows of 8 of tuples i.e. ("date", "price")
        length = len(self.data)
        if (start > length and end > length):
            print("Invalid range entered!")
            return

        if (start < 0):    # Start must be >= 0
            start = 0
        if (end > length): # End must be <= len(self.data)
            end = length
        if (start > end):  # Swap if start > end
            temp = end
            end = start
            start = temp

        print( "TICKER:\t {}".format(self.ticker) )
        print( "INDICATOR:\t {}\n".format(self.indicator) )
        counter = 0
        for i in range(start, end):
            if (counter % 8 == 0):
                print("")
            print(self.data[i])
            counter += 1
