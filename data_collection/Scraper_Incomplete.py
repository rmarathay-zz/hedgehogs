import requests
import json
import psycopg2
import io
from lxml import html
from time import sleep

#######################################################################################

"""
Issues:
    (1) Will only grab 100 days worth of stock data.
    Fix: Find a way on Yahoo Finance to set the date range of the data
         to max and then 'click' apply to confirm the changes, from there
         more data will be loaded so it will scrape more than 100 days.

Functionality:
    This script will read in a text file with company tickers (ex. TSLA) and
    construct a custom url on Yahoo Finance and scrape data into a dictionary.
    As of now, it only has [DATE, OPEN, HIGH, LOW, CLOSE, ADJ CLOSE, VOLUME].

    The order of the data is from most recent day to past.
"""

#######################################################################################

def json_format(data):
    """
    * This function takes in the raw scraped data and transforms it
    * into json format so that it can be loaded into the database.
    """

    string = json.dumps(data)
    loaded_json = json.loads(string)
    print(loaded_json)
    return loaded_json

#######################################################################################

def connect_and_send(data, stock):
    """
    * This function takes in a stock ticker and its respective data and loads the
    * database and then sends the data to it
    """

    conn = None
    try:
        # Connect to the PostgreSQL server.
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(host='206.189.181.163',
                            database="rcos",
                                user="rcos",
                            password="hedgehogs_rcos")

        # Create a cursor and execute query.
        cur = conn.cursor()
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        #
        #send_input(cur)
        #

        # SQL command setup to create table and execute the command with stock in string.
        temp = ("CREATE TABLE %s(date TIMESTAMP, low double precision, high double precision, volume double precision, close double precision, open double precision);" % stock)
        cur.execute(temp)


        for date in dates:
            insert = ("INSERT INTO {}(date,low,high,volume,close,open) VALUES ('{}', {}, {}, {}, {}, {})"
            .format(symbol, date,
                        data['Time Series (Daily)'][str(date)]['3. low'],
                        data['Time Series (Daily)'][str(date)]['2. high'],
                        data['Time Series (Daily)'][str(date)]['5. volume'],
                        data['Time Series (Daily)'][str(date)]['4. close'],
                        data['Time Series (Daily)'][str(date)]['1. open']))
            cur.execute(insert)


## THIS CODE IS USED AFTER ALL DATA IS EXECUTED

        conn.commit()

        # Display the PostgreSQL database server version.
        db_version = cur.fetchone()
        print(db_version)
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

#######################################################################################

if __name__ == "__main__":
    base_url = 'http://finance.yahoo.com/quote/%s/history?p=%s'
    table_xpath = '//table[contains(@data-test,"historical-prices")]//tr'
    data_xpath = '//td[contains(@class,"Py(10px) Pstart(10px)")]//text()'
    date_xpath = '//td[contains(@class,"Py(10px) Ta(start) Pend(10px)")]//text()'

    # Open file and check to see that it's opened correctly
    try:
        file = open("stocks.txt", "r")
    except IOError:
        print("Couldn't open stocks.txt to read!")
    else:
        print("Input file opened successfully!")
    tickers = [line.rstrip() for line in file]

    # Build the URL for each stock and begin accessing data
    #for stock in stocks:
    for i in range(1):
        ticker = tickers[i]
        custom_url = base_url % (ticker, ticker)
        print("Building URL: <", custom_url, ">", sep="")
        req = requests.get(custom_url)
        sleep(2)

        # Throw an exception if unable to reqest url
        if (req.status_code != requests.codes.ok):
            raise Exception("Unable to access <", custom_url, ">", sep="")

        # Gets HTML file in a tree structure, retrieve data from table
        # Then set data to max number and apply the changes...
        tree = html.fromstring(req.text)
        historical_table = tree.xpath(table_xpath)
        if not historical_table:
            raise Exception("Could not follow XPath!")
        else:
            print("Acessing", len(historical_table), "data entries...\n")

        day = 0
        idx = 0
        out_data = {}

        for table_data in historical_table:
            # Accesses a list of all of the date data
            data = table_data.xpath(data_xpath)
            if (day == 0):
                date = table_data.xpath(date_xpath)

            # Data is presented as 6 data points per day
            # [Open] [High] [Low] [Close] [Adj Close] [Volume]
            if (day < 99): # Change this number if you're able to collect more data...
                out_data[day] = []
                out_data[day].append(date[day])
                for i in range(6):
                    try:
                        out_data[day].append(data[idx])
                    except:
                        print("Cannot access data...")
                    idx += 1
                day += 1


        loaded_json = json_format(out_data)
        print(loaded_json)


        # MAKE A FUNCTOIN CALL TO CONNECT AND THEN SAVE THE DATA
        # THIS FUNCTION IS connect_and_send ...
