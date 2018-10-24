import psycopg2
from connection import connection
from pandas_datareader import data, wb
import pandas_datareader.data as web
import datetime

def makeRow(symbol, f, date_list):
    ret = []
    for date in date_list:
        row = [symbol, date]
        row.append(float(f.loc[date,"Open"]))
        row.append(float(f.loc[date,"High"]))
        row.append(float(f.loc[date,"Low"]))
        row.append(float(f.loc[date,"Close"]))
        row.append(int(f.loc[date,"Volume"]))
        ret.append(row)
    return ret

if __name__ == "__main__":

    start = datetime.datetime(2017,1,1)
    #watchlist = set(["AAPL", 'AMD', 'AMZN', 'ATVI', 'BABA', 'BAC', 'BLK', 'BWLD', 'CELG', 'CRM', 'F', 'FB','GOOG','IBM','INTC','JPM','KORS','LMT','LULU','MOMO','MSFT','MU','NFLX','NKE','NVDA','PCLN','PFE','RTN','SBUX','SHOP','SNAP','SPY','SQ','TAP','TSLA','ULTA','V','VOO','VOOG','VXX'])
    watchlist = set(['AAPL', 'NFLX', 'BABA'])
    curr = 1
    tot = len(watchlist)
    biglist = []

    for symbol in watchlist:
        connected = False
        i = 1
        while not connected and i < 4:
            try:
                f = web.DataReader(symbol.lower(), 'yahoo', start)
                print("connected ",symbol,'(',curr,' of ',tot,')')
                curr += 1
                connected = True
            except Exception as e:

                print("couldn't connect to data for: ",symbol, ' (Attempt number ', i,')',sep='')
                i += 1
                continue

        l = []
        for index in f.index:
            l.append(index.strftime('%Y-%m-%d'))

        attempts_sql = 1
        insql = False
        while not insql and attempts_sql < 4:
            try:
                results = makeRow(symbol, f, l)
                biglist.extend(results)
                print(results)
                insql = True
            except Exception as e:
                print("couldn't add ", symbol, ' to mysql (Attempt number ',attempts_sql,')',sep='')
                attempts_sql += 1
                continue


    # Postgres
    # conn is connection c is cursor
    con, c = connection()
    c.execute("""Create table tmp""")

    # TODO: NEED TO ADD TMP SCHEMA HERE

    for row in biglist:
        try:
            c.execute(""""INSERT into tmp (primary_key, symbol, date, open, high, low, close, volume) values (0, %s, %s, %s, %s, %s, %s, %s)""",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],))
            con.commit()
        except Exception as e:
            print(e)
            con.rollback()

    con.close()
