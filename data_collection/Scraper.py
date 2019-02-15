import sys
import requests
import json
import psycopg2
from datetime import datetime
def get_company_info(symbol):
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+ symbol + "&apikey=1BGCK5RG5D5CQCAJ&datatype=json"
    response = json.loads(requests.get(url).text)
    return response
def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
 
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host='206.189.181.163',
                            database="rcos",
                                user="rcos",
                            password="hedgehogs_rcos")
 
        # create a cursor
        cur = conn.cursor()
        
        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        #Send cursor over to read_input to process tickers
        read_input(cur)

        conn.commit()
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
        # close the communication with the PostgreSQL
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def read_input(cur):
    lines = [line.rstrip('\n') for line in open('companies.txt')]
    for symbol in lines:
        data = get_company_info(symbol)
        dates = []
        for entry in data['Time Series (Daily)']:
            dates.append(entry)
        dates.sort(key = lambda date: datetime.strptime(date, '%Y-%m-%d'))
        temp = ("CREATE TABLE %s(date TIMESTAMP, low double precision, high double precision, volume double precision, close double precision, open double precision);")

        cur.execute(temp, symbol)
        insert_st = ("INSERT INTO %s(date,low,high,volume,close,open) VALUES (%s, %f, %f, %f, %f, %f)")
        for date in dates:
            temp_info = (date, 
                        data['Time Series (Daily)'][str(date)]['3. low'],
                        data['Time Series (Daily)'][str(date)]['2. high'],
                        data['Time Series (Daily)'][str(date)]['5. volume'],
                        data['Time Series (Daily)'][str(date)]['4. close'],
                        data['Time Series (Daily)'][str(date)]['1. open'])
            cur.execute(insert_st, temp_info)

        #for date in dates:
         #   print(date, ": closed at",data['Time Series (Daily)'][str(date)]['4. close'])
 

if __name__ == "__main__":
    connect()
    