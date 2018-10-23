
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
	(conn, cur) = connection()
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

