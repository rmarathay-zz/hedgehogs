"""
This class is meant to replicate an actual stock trader or client who
wishes to test their trading algorithm on our historical data. As of now,
this object features initialization, buy, and sell features.

TODO: Need to integrate this with StockData object and trading rules
"""

class ClientTrader:


    def __init__(self, name, capital):
        """
        Constructor to create ClientTrader object.

        Arguments:
            self.name: stores the name of the client trader
            self.capital: stores the current funds available for investment
            self.buy: keeps track of tuple of (DATE, PRICE_AT_BUY_TIME)
            self.sell: keeps track of tuple of (DATE, PRICE_AT_SELL_TIME)
        """
        self.name = name
        self.capital = capital
        self.buy = []
        self.sell = []


    def buyStock(self, ticker, date, price):
        """
        Checks to see if the client has sufficient funds to purchase the stock.
        If so, the stock is purchased but if not a message is printed.

        Arguments:
            ticker: the stock name
            date: the date of the desired buy
            price: the current price of the stock
        """
        delta = self.capital - price
        if (abs(delta) == delta):
            self.capital = self.capital - price
            stockInfo = (date, price)
            self.buy.append(stockInfo)
            print("Purchase complete!")
            print("\tPrice of stock:  ", price)
            print("\tFunds available: ", self.capital)
        else:
            print("Insufficient funds!")


    def sellStock(self, ticker, date, price):
        """
        Sells the desired stock and the funds are added back to self.capital

        Arguments:
            ticker: the stock name
            date: the date of the desired sell
            price: the price of the stock being sold
        """
        self.capital = self.capital + price
        stockInfo = (date, price)
        self.sell.append(stockInfo)
        print("Completed transaction of ",ticker,"!",sep="")
        print("Funds available: ", self.capital)
