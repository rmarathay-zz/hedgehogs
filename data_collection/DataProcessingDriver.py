import psycopg2
import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt
from psycopg2 import Error
from DataProcessing import StockData
import displayData



def pullColumnAll(cursor, ticker, column_name):
    """
    Retrieves specific column data for the given parameter (column_name)

    Arguments:
        cursor: cursor object for the database
        ticker: ticker for which we are collecting data
        column_name: specific column we want data from

    Returns:
        column data for the selected column name and the dates associated
    """
    DATE_TABLE_QUERY = ('SELECT date FROM {}'.format(ticker))
    DATA_TABLE_QUERY = ('SELECT {} FROM {}'.format(column_name, ticker))
    print("Your query: ", '\'', DATE_TABLE_QUERY, '\'', sep="")
    print("Your query: ", '\'', DATA_TABLE_QUERY, '\'', sep="")

    cursor.execute(DATE_TABLE_QUERY)
    column_dates = cursor.fetchall()
    cursor.execute(DATA_TABLE_QUERY)
    column_data = cursor.fetchall()

    dates = [d for d in column_dates]
    data = [d for d in column_data]
    return dates, data



def pullColumnRange(cursor, ticker, column_name, start, end):
    """
    Retrieves specific column data over an interval start-ending

    NOTE: end must be a later date then start, and in the form timestamp
        i.e. start := '2010-08-08 00:00'
               end := '2011-08-08 00:00'

    Arguments:
        cursor: cursor obj for database
        ticker: ticker for which we are collecting
        column_name: indicator
        start: start interval
        end: end interval

    Returns:
        Column data for the given indicator as a list
        Length of this list = end-start
    """

    try: # Trust user and try from the start date to the end date
        DATE_TABLE_QUERY = ('SELECT date FROM {} WHERE date >= {} AND < {}'.format(ticker, start, end))
        DATA_TABLE_QUERY = ('SELECT {} FROM {} WHERE date >= {} AND < {}'.format(column_name, ticker, start, end))
        cursor.execute(DATE_TABLE_QUERY)
        column_dates = cursor.fetchall()
        cursor.execute(DATA_TABLE_QUERY)
        column_data = cursor.fetchall()
    except (Exception, psycopg2.DatabaseError) as error:
        pass

    try: # Try from start date the the end of available data
        DATE_TABLE_QUERY = ('SELECT date FROM {} WHERE date >= {}'.format(ticker, start))
        DATA_TABLE_QUERY = ('SELECT {} FROM {} WHERE date >= {}'.format(column_name, ticker, start))
        cursor.execute(DATE_TABLE_QUERY)
        column_dates = cursor.fetchall()
        cursor.execute(DATA_TABLE_QUERY)
        column_data = cursor.fetchall()
    except:
        pass

    try:
        dates, data = pullColumnAll(cursor, ticker, column_name)
        return dates, data
    except (Exception, psycopg2.DatabaseError) as error:
        print("Unknown error, aborting program!")

    print("Your query: ", '\'', DATA_TABLE_QUERY, '\'', sep="")
    print("Your query: ", '\'', DATE_TABLE_QUERY, '\'', sep="")
    dates = [d for d in column_dates]
    data = [d for f in column_data]
    return dates, data



if __name__ == '__main__':

    connection = None
    try:
        # Connect to the PostgreSQL Server & Databse
        print('Connecting to the PostgreSQL database...')
        connection = psycopg2.connect(host='206.189.181.163',
                                database='rcos',
                                user='rcos',
                                password='hedgehogs_rcos')

        # Create a Cursor & Print Version
        cursor = connection.cursor()

        # Print PostgreSQL Version
        print('PostgreSQL database version:', cursor.execute('SELECT version();'))
        record = cursor.fetchone()
        print('You are connected to - ', record, '\n')
        print("COLUMN NAME OPTIONS:")
        print("\tdate\n\tlow\n\thigh\n\tvolume\n\tclose\n\topen\n")

        # Example for Ticker AAPL
        ticker = "aapl"
        column_name = "open"
        dates, data = pullColumnAll(cursor, ticker, column_name)
        print("data size: {}\ndates size: {}".format(len(data), len(dates)))

        # Example Moving Averages for APPL
        window_sma = 50
        window_ema = 10
        AAPL = StockData(ticker, column_name, dates, data)
        print("\nChecking ticker", AAPL.getTicker(), "for column:", AAPL.getIndicator())
        print("SMA:", AAPL.simpleMA(window_sma))
        #print("\nEMA:", AAPL.expMA(window_ema))
        print("")
        dates, close = pullColumnAll(cursor, ticker, "close")
        displayData.plotClose(dates, close)

        # Test Accessor Methods
        #print("Maximum value:", AAPL.getMax())
        #print("Median value:", AAPL.getMedian())
        #print("Time range:", AAPL.getTimeRange())

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL =>", error)

    finally:
    #Closing Database Connection
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")

################################################################################
