"""
addToPostgres.py
This file adds eod stock price data to our postgres database

The database configuration is pulled from config.py and the
stock tickers are pulled from the desired text file

TODO: We should make this work asynchronously.
Right now, the program downloads all data and stores it in memory
in rowsList. It would make more sense to be downloading the data and
simultaneously adding it to the database.
This would drastically reduce our space complexity.
"""

import psycopg2
from connection import connection
from pandas_datareader import data, wb
import pandas_datareader.data as web
import datetime

# This function creates a valid row for our database


def makeRow(symbol, f, date_list):
    ret = []
    for date in date_list:
        row = [symbol, date]
        row.append(float(f.loc[date, "Open"]))
        row.append(float(f.loc[date, "High"]))
        row.append(float(f.loc[date, "Low"]))
        row.append(float(f.loc[date, "Close"]))
        row.append(int(f.loc[date, "Volume"]))
        ret.append(row)
    return ret

# This function initializes our table under the given name


def init_table(db, c, tableName, sequenceName):
    """
    @params
    db              database connection object
    c               database cursor
    tableName       string        name of table to initialize
    sequenceName    string        name of sequence to initialize

    This function creates a new table on the provided db with
    the eod format as shown
    """
    print("[LOG] creating table {}".format(tableName))

    # First try and make the sequence that will be used for primary key
    try:
        print("[LOG] Creating sequence {}".format(sequenceName))
        c.execute("create sequence {} start 1 increment 1;".format(sequenceName))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

    # Next we try and create our table
    try:
        c.execute("Create table {} (    \
            primary_key     serial PRIMARY KEY,\
            symbol          varchar(7), \
            date            date,       \
            open            float(4),   \
            high            float(4),   \
            low             float(4),   \
            close           float(4),   \
            volume          int \
            );".format(tableName))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()


if __name__ == "__main__":

    # We will add data starting from this date
    start = datetime.datetime(2017, 1, 1)

    # The watchlist is located in sampleWatchlist.txt
    # A longer watchlist is in sp500.txt
    f1 = open("sampleWatchlist.txt", "r")

    # Initialize a set of unique tickers from the watchlist
    watchlist_f = set(f1.read()[1:-1].strip('""').split("', '"))

    # rowsList will hold the data we parse from yahoo finance
    rowsList = []

    curr = 1
    tot = len(watchlist)

    # Data collection

    # We will loop through each ticker on the watchlist and create
    # rows of data for it
    for symbol in watchlist:
        connected = False
        i = 1
        # We will try 3 times to get data from yahoo finance
        # if this fails 3 times, we can safely assume the stock
        # has changed tickers or is otherwise not on yahoo finance
        while not connected and i < 4:
            try:
                f = web.DataReader(symbol.lower(), 'yahoo', start)
                print("connected ", symbol, '\t\t(', curr, ' of ', tot, ')')
                curr += 1
                connected = True
            except Exception as e:
                print("couldn't connect to data for: ", symbol,
                      ' (Attempt number ', i, ')', sep='')
                i += 1
                continue

        # L is a list of valid stock market dates
        l = []
        for index in f.index:
            l.append(index.strftime('%Y-%m-%d'))

        attempts_sql = 1
        insql = False
        while not insql and attempts_sql < 4:
            try:
                results = makeRow(symbol, f, l)
                rowsList.extend(results)
                # print(results)
                insql = True
            except Exception as e:
                print("couldn't add ", symbol,
                      ' to mysql (Attempt number ', attempts_sql, ')', sep='')
                attempts_sql += 1
                continue

    # Postgres

    tableName = "eod_tmp1"
    sequenceName = "quote_id"

    # db is connection c is cursor
    db, c = connection()

    # When adding all of the data, we may want to reinitialize the table
    # This avoids adding duplicate data
    # Here we drop the table
    try:
        print("[LOG] Dropping table {}").format(tableName)
        c.execute("drop table {};".format(tableName))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

    # Here we get rid of the primary_key sequence
    try:
        print("[LOG] Dropping sequence {}".format(sequenceName))
        c.execute("drop sequence {};".format(sequenceName))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

    # Here we make a new table
    try:
        init_table(db, c, tableName, sequenceName)
    except Exception as e:
        print(e)
        db.rollback()

    # Add each row that we collected in the data_collection section
    for row in rowsList:
        try:
            c.execute("INSERT into {} (primary_key, symbol, date, open, high, low, close, volume) values (nextVal('{}'), '{}', to_date('{}','YYYY-MM-DD'), {}, {}, {}, {}, {});"
                      .format(tableName, sequenceName, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()

    db.close()
