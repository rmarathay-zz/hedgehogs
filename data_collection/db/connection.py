import psycopg2

def connection():
    """
    Function to connect to our local PostgreSQL database
    :returns a database connection conn and a cursor cur
    """
    print('[LOG] Trying to connect')

    conn = None
    try:
        #conn = psycopg2.connect("host=206.189.181.163 port=5432")
        conn = psycopg2.connect("host=192.168.99.100 port=5432 user=rcos password=password")
        cur = conn.cursor()
        print('[LOG] Connected!')
        return conn, cur
    except:
        print("[ERROR] Unable to connect. Returning error..")
        return -1, -1

if __name__ == "__main__":
    connection()
