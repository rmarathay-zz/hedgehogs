# * ProvisionSchema happens first (initializes the database for Scraper)
# * Creates necessary schemas
import psycopg2
import sys

#Return a connection object with the database
def connectDB(pass):
	try:
		conn = psycopg2.connect(host="206.189.181.163", dbname="rcos", user="rcos", password=pass)
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
	return conn

#Close the connection with the database
def closeDB(conn):
	print("Attempting to close connection with database")
	if (conn!=None):
		print("Connection successfully closed")
		conn.close()

	else:
		print("Database connection already closed")

#Ensure a table with the naem doesn't already exist
def verifyTableName(cursor,tableName):
	cursor.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
	if tableName in cursor.fetchAll():
		return tableName
	else:
		print("Table with name " + tableName + " already exists!")
		return "invalid"

#Restart the database connection when needed
def restartDB(conn):
	print("Beginning connection restart")
	closeDB(conn)
	conn = connectDB()
	return conn

def validateConn(conn):
	for i in range(4):
		if (conn.closed==0):
			return True
		else:
			if (i==3):
				return False
			conn = restartDB(conn)
			cursor = conn.cursor()
#Prepare the database by creating the table
def prepDB(conn, cursor, tableName):
	#Try to restart connection if dead
	if (validateConn(conn)==False):
		sys.exit("Unable to recover database connection")
	try:
		cursor.execute("CREATE TABLE {} (    \
				open            float(4),   \
				high            float(4),   \
				low             float(4),   \
				close           float(4),   \
				volume          int \
				);".format(tableName))
		conn.commit()
		conn.close()
	except Exception as error:
		print(error)
		conn.rollback()
		closeDB(conn)

def main():
	if (len(sys.argv)<3):
		sys.exit("Must provide at least one table name")
	conn = connectDB(sys.argv[1])
	cursor = conn.cursor()
	for i in range(len(sys.argv)):
		tableName = verifyTableName(cursor, sys.argv[i])
		if (tableName=="invalid"):
			continue
		prepDB(conn, cursor, tableName)

if __name__ == '__main__':
	main()

