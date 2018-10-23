import MySQLdb
import _mysql
from MySQLdb.constants import FIELD_TYPE
from pandas_datareader import data, wb
import pandas_datareader.data as web
import datetime
from multiprocessing.pool import ThreadPool
from multiprocessing import Pool
from functools import partial


def makeRow(symbol, f, date):
    row = [symbol, date]
    row.append(float(f.loc[date,"Open"]))
    row.append(float(f.loc[date,"High"]))
    row.append(float(f.loc[date,"Low"]))
    row.append(float(f.loc[date,"Close"]))
    row.append(int(f.loc[date,"Volume"]))
    return row
        
if __name__ == "__main__":
    
    start = datetime.datetime(2017,1,1)
    #watchlist = ['AAPL', 'BABA']
    watchlist = set(["AAPL", 'AMD', 'AMZN', 'ATVI', 'BABA', 'BAC', 'BLK', 'BWLD', 'CELG', 'CRM', 'F', 'FB','GOOG','IBM','INTC','JPM','KORS','LMT','LULU','MOMO','MSFT','MU','NFLX','NKE','NVDA','PCLN','PFE','RTN','SBUX','SHOP','SNAP','SPY','SQ','TAP','TSLA','ULTA','V','VOO','VOOG','VXX'])
    
    f1 = open("sp500.txt","r")
    watchlist2 = set(f1.read()[1:-1].strip('"').split("', '"))  
    
    watchlist_f = watchlist | watchlist2
    biglist = []
    
    curr = 1
    tot = len(watchlist_f)
    for symbol in watchlist_f:
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
        #print(makeRow('2017-11-22'))
        #print(makeRow(l[0]))
        attempts_sql = 1
        insql = False
        while not insql and attempts_sql < 4:
            try:
                func = partial(makeRow, symbol, f)
                p = Pool()
                results = p.map(func, l)
                
                p.close()
                p.join()
                biglist.extend(results)
                insql = True
            except Exception as e:
                print("couldn't add ", symbol, ' to mysql (Attempt number ',attempts_sql,')',sep='')
                attempts_sql += 1
                continue
        
    #SQL
    db = MySQLdb.connect(host='localhost',user='root',passwd='roott',db='stocks')
    c = db.cursor()
    #c.execute("""truncate data""")
    db.commit()
    for row in biglist:
        try:
            c.execute("""INSERT into big_data (primary_key, symbol, date, open, high, low, close, volume) values (0, %s, %s, %s, %s, %s, %s, %s)""",(row[0],row[1],row[2],row[3],row[4],row[5],row[6],))
            db.commit()
        except:
            db.rollback()
    db.close()        
        
    