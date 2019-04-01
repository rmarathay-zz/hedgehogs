import psycopg2
import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt
from psycopg2 import Error
from DataProcessing import StockData
import displayData


def pullColumn(cursor, ticker, column_name):
    """
        
    retrieves specific column data for the given parameter (column_name)

    Arguments:
        cursor: cursor object for the database
        ticker: ticker for which we are collecting data
        column_name: specific column we want data from

    Returns:
        column data for the selected column name

    """
    TABLE_QUERY = ('SELECT {} FROM {}'.format(column_name, ticker))
    print("Your query: ", '\'', TABLE_QUERY, '\'', sep="")
    cursor.execute(TABLE_QUERY)
    column_data = cursor.fetchall()
    return_list = []
    for i in column_data:
        return_list.append(i[0])
    return return_list


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

        # Print PostgreSQL version
        print('PostgreSQL database version:', cursor.execute('SELECT version();'))
        record = cursor.fetchone()
        print('You are connected to - ', record, '\n')

        print("COLUMN NAME OPTIONS:")
        print("\tdate\n\tlow\n\thigh\n\tvolume\n\tclose\n\topen\n")

        ticker = "aapl"
        column_name = "open"
        data = pullColumn(cursor, ticker, column_name)
        dates = pullColumn(cursor, ticker, "date")
        print("data size: {}\ndates size: {}".format(len(data), len(dates)))

        print("\nTESTING...")
        window_sma = 50
        window_ema = 10
        AAPL = StockData(ticker, column_name, dates, data)
        print(AAPL.getTicker())
        print(AAPL.getIndicator())
        print("SMA:", AAPL.simpleMA(window_sma))  # should have 5 data points
        print("\nEMA:", AAPL.expMA(window_ema))     # should have 20 data points
        print("")
        print("Maximum value:", AAPL.getMax())
        print("Median value:", AAPL.getMedian())
        print("Time range:", AAPL.getTimeRange())
        cl = pullColumn(cursor, ticker, "close")
        displayData.plotClose(dates, cl)



    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
    #Closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")

################################################################################
