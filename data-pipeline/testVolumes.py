import psycopg2
from connection import connection
from pandas_datareader import data, wb
import pandas_datareader.data as web
import datetime

if __name__ == "__main__":

    print("Testing db volumes")

    # db is connection and c is cursor to db
    db, c = connection()

    print("[LOG] creating table")
    try:
        c.execute("drop table tmp")
        c.execute("drop sequence tmp_sequence")
        c.execute("Create table tmp (\
            ID          serial PRIMARY KEY,\
            col2        int,\
            col3        int\
            );")
        c.execute("Create sequence tmp_sequence start 1 increment 1;")
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

    print("[LOG] adding row to table")
    try:
        c.execute("insert into tmp \
        ( ID, col2, col3)\
        values\
            (nextval('tmp_sequence'), 100, 200);")
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

    print("[LOG] closing connection")
    db.close()
