"""
updatePostgres.py
This file adds only the missing stock data to our postgres db

It first checks the most recent date that we already have in the db,
then fills from that date up until today
"""

import psycopg2
import pandas_datareader.data as web
import datetime
import sys
from addToPostgres import makeRow
from connection import connection

# This function grabs the highest primary key from the table and starts
# the sequence at sequenceName at this value


def reinitSequence(db, c, sequenceName, tableName):
    c.execute("select max(primary_key) from {}".format(tableName))
    max = c.fetchone()[0]

    try:
        print("[LOG] Dropping sequence {}".format(sequenceName))
        c.execute("drop sequence {}".format(sequenceName))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

    try:
        print("[LOG] Reinitializing sequence {}".format(sequenceName))
        c.execute("Create sequence {} start {} increment 1;"
                  .format(sequenceName, max))
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()


if __name__ == "__main__":

    tableName = "eod_tmp1"
    sequenceName = "quote_id"

    # db is connection c is cursor
    db, c = connection()

    # we want to grab the highest primary_key in the table currently
    '''
    These lines find the latest date in the database
    and make sure we add starting from the next day
    '''
    c.execute("select max(date) from {}".format(tableName))
    start = c.fetchone()[0] + datetime.timedelta(days=1)

    print("[LOG] Adding data starting from {}".format(start))

    now = datetime.datetime.now()
    today = now.date()
    if start > today or ((start == today) and now.hour < 17):
        print("[LOG] No data to add!\n[LOG] Exiting!")
        sys.exit()

    f1 = open("sampleWatchlist.txt", "r")
    watchlist_f = set(f1.read()[1:-1].strip('"').split("', '"))

    biglist = []

    curr = 1
    tot = len(watchlist_f)
    # We loop through each symbol in the watchlist to gather it's data
    for symbol in watchlist_f:
        if len(symbol) == 0:
            continue
        connected = False
        i = 1
        while not connected and i < 4:
            try:
                f = web.DataReader(symbol.lower(), 'yahoo', start)
                print("connected ", symbol, '(', curr, ' of ', tot, ')')
                curr += 1
                connected = True
            except Exception as e:

                print("couldn't connect to data for: ", symbol,
                      ' (Attempt number ', i, ')', sep='')
                i += 1
                continue
        l = []
        for index in f.index:
            l.append(index.strftime('%Y-%m-%d'))

        attempts_makeRow = 1
        rowMade = False
        while not rowMade and attempts_makeRow < 4:
            try:
                results = makeRow(symbol, f, l)
                biglist.extend(results)
                rowMade = True
            except Exception as e:
                print("couldn't add ", symbol,
                      ' to postgres (Attempt number ', attempts_makeRow, ')', sep='')
                attempts_makeRow += 1
                continue

    # Postgres

    # We don't want to reinitialize the table here, instead we
    # add the data we just collected

    #reinitSequence(db, c, sequenceName, tableName)

    for row in biglist:
        try:
            c.execute("INSERT into {} (primary_key, symbol, date, open, high, low, close, volume) values (nextVal('{}'), '{}', to_date('{}','YYYY-MM-DD'), {}, {}, {}, {}, {});"
                      .format(tableName, sequenceName, row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()

    db.close()
