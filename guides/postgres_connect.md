# PostgreSQL on Hedgehogs:


##### How to Connect on Terminal:
You will need to install pgcli:

```
pip install pgcli
```

Once complete in the terminal type:

```
pgcli postgres://rcos:hedgehogs_rcos@206.189.181.163:5432
```

When prompted, enter password (Ask Ranjit)


#### How to Connect on python:
In order to create scripts on python for Postgres, you will need to install psycopg2


To create a connection (conn) with its respective cursor:
```
def connection():
    print('[LOG] Trying to connect')
    try:
        conn = psycopg2.connect("host=206.189.181.163 port=5432 user=rcos password=hedgehogs_rcos dbname=rcos")
        cur = conn.cursor()
        print('[LOG] Connected!')
        return conn, cur
    except:
        print("[ERROR] Unable to connect. Quitting...")
```