# Psycopg2 Example - A Way to Run SQL Scripts on Python


##### Prerequisites:
You will need to install psycopg2:

```
pip install psycopg2
```

#### How to Connect on Python (Review):

From the connection tutorial, there was this function:

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

- Psycopg2.connect returns a connection object, which encapsulates the database session. This will be the base for every start of a script. Our example has the host IP address and port, username and password, and the database name.

- Following the connection object, connection.cursor() returns a cursor object. All you need to know about this is that this is what allows us to execute postgreSQL commands in a session. The cursor will be bound to the connection for the duration of the session.

#### Create a Table:

Now that we have a connection, let's create a table to work with:
```
(conn, cur) = connection()
cur.execute("""
CREATE TABLE test(
	id text PRIMARY KEY,
	name text)
	""")
conn.commit()
```
- As mentioned before, we will utilize the cursor object, and call it's function: "Cursor.execute()". This is the bread and butter of psycogp2, allowing us to write in plaintext string, what we would normally write in SQL. (I have an SQL Guide ready on this directory with resources linked, if you haven't already seen it.)

- In this example, we created a table (CREATE TABLE) with name test, which has an identifier named PRIMARY KEY, and the name of company.

- Do not forget to commit from the connection (not the cursor since you are not writing anything, its the connection's job now). This basically takes the cursor's work and actually commits it onto the database. Without this step, you will not update the database.


#### Pushing onto Table:

Now let's take what we've learned and push data into the table while parsing data:

```
import csv

def generate_uuid():
	return uuid.uuid4()


f = open("finsim.csv")
csv_f = csv.reader(f)

checked = []
isFirstRow = True
for row in csv_f: 
	if(isFirstRow): #ignore first row of categories
		isFirstRow = False 
		continue

	if( not (row[0] in checked) ): #Push unique IDs only
		d = str(generate_uuid())
		checked.append(row[0])
		cur.execute("INSERT INTO company_table (company_id, ticker, ticker_id) VALUES (%s,%s,%s)"
				,(d , row[0], row[1]))

conn.commit()
```
- Each dataset is formatted differently, and this one is for finsim's csv files. The parsing part should be matched for your specific dataset. Here, there was some disclaimer information on the top, so I skip the first row of the CSV file.

- The goal of this script is to add details like the ticker name, company name, but I added a UUID portion to make sure we have unique identifers for the table.

- Our data repeats company names, because at each line it shows a different statistic. We don't need that much information right now, so I just created a way to push a company onto the table if we haven't encountered it yet.


#### Full Code:
In case you want to manipulate certain parts:

##### WARNING: Please do not run this with the connecting details below, it will either override our current table, or corrupt our schemas that we have already set up. I reccomend booting a local server instance of postgresql on the terminal and just testing there. This is mainly for final commits that are finished.

```
import csv
import psycopg2
import uuid
import sys


def connection():
    print('[LOG] Trying to connect')
    try:
        conn = psycopg2.connect("host=206.189.181.163 port=5432 user=rcos password=hedgehogs_rcos dbname=rcos")
        cur = conn.cursor()
        print('[LOG] Connected!')
        return conn, cur
    except:
        print("[ERROR] Unable to connect. Quitting...")

def generate_uuid():
	return uuid.uuid4()



if __name__ == '__main__':

	print(str(generate_uuid()))
	# (conn, cur) = connection()
	# cur.execute("""
	# CREATE TABLE test(
	# 	id text PRIMARY KEY,
	# 	name text
	# )
	# 	""")
	# conn.commit()

	csv.field_size_limit(sys.maxsize)
	f = open("finsim.csv")
	csv_f = csv.reader(f)

	checked = []
	isFirstRow = True
	for row in csv_f: #ignore first row of categories
		if(isFirstRow):
			isFirstRow = False 
			continue

		if( not (row[0] in checked) ): #Push unique IDs only
			d = str(generate_uuid())
			checked.append(row[0])
			cur.execute("INSERT INTO company_table (company_id, ticker, ticker_id) VALUES (%s,%s,%s)"
					,(d , row[0], row[1]))

	conn.commit()
```