import psycopg2
import numpy as np
from numpy import convolve
import matplotlib.pyplot as plt
from psycopg2 import Error
import displayData

################################################################################

def pullColumn(cursor, ticker, column_name):
    # column_name expects [date, open, close, high, low, volume]
    # @params: a stock ticker
    # @params: a database cursor and a column name to take data
    # @returns: column data for the selected column name

    TABLE_QUERY = ('SELECT {} FROM {}'.format(column_name, ticker))
    print("Your query: ", '\'', TABLE_QUERY, '\'', sep="")
    cursor.execute(TABLE_QUERY)
    column_data = cursor.fetchall()
    return_list = []
    for i in column_data:
        return_list.append(i[0])
    return return_list

################################################################################

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
        open = pullColumn(cursor, ticker, "open")
        close = pullColumn(cursor, ticker, "close")
        high = pullColumn(cursor, ticker, "high")
        low = pullColumn(cursor, ticker, "low")
        dates = pullColumn(cursor, ticker, "date")
        #print("data size: {}\ndates size: {}".format(len(data), len(dates)))

        displayData.plotCandleStick(dates, open, close, high, low)


    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
    #Closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")

################################################################################