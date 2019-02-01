import psycopg2
from config import make_conn_string


def connection():
    """
    Function to connect to our local PostgreSQL database
    :returns a database connection conn and a cursor cur
    """
    print('[LOG] Trying to connect')

    conn = None
    try:
        conn = psycopg2.connect(make_conn_string())
        cur = conn.cursor()
        print('[LOG] Connected!')
        return conn, cur
    except Exception as e:
        print(e)
        print("[ERROR] Unable to connect. Returning error..")
        return -1, -1


if __name__ == "__main__":
    connection()
