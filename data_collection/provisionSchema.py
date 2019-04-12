# * ProvisionSchema initializes the database for Scraper. Arguments in order are db_password, name1, name2,..., namek
import psycopg2
import sys
from simpleParser import getPasswordDB

def connectDB(secret):
	"""

	connectDB attempts to create a connection with the database
    
    Args:
        secret: The password used to authenticate
    
    Returns:
        A new connection object (to the PostgreSQL server)
    
    """
	try:
		conn = psycopg2.connect(host="206.189.181.163", dbname="rcos", user="rcos", password=secret)
	except (Exception, psycopg2.DatabaseError) as error:
		print(error)
		sys.exit(1)
	return conn

def closeDB(conn):
	"""

	closeDB attempts to close the connection (make it unusable)
    
    Args:
        conn: The connection object that will be closed
    
    """
	print("Attempting to close connection with database")
	if (conn!=None):
		print("Connection successfully closed")
		conn.close()
	else:
		print("Database connection already closed")

def createSchema(conn, cursor, companyName):
	"""

	createSchema creates the schema and creates a table for each company
	
	Args:
		cursor: The cursor to the current database session
        conn: The connection object to the current database session
        companyName: list of company names
	
	"""
	sql = "CREATE SCHEMA stockData AUTHORIZATION rcos"
	try:
		cursor.execute(sql)
		conn.commit()
	except Exception as e:
		print(e)
		conn.rollback()
	for i in range(0, len(companyName)):
		createTable = "CREATE TABLE IF NOT EXISTS stockData.{} (    \
				id		serial PRIMARY KEY,\
				date 			date, 		\
				open            float(4),   \
				high            float(4),   \
				low             float(4),   \
				close           float(4),   \
				volume          int \
				);".format(tableName[i])
		try:
			cursor.execute(createTable)
			conn.commit()
		except Exception as e:
			print(e)
			conn.rollback()

def main():
	"""
	
	program flow for provisionSchema (must provide at least one ticker to create table)


	"""
	if (len(sys.argv)<2):
		sys.exit("Must provide at least one table name")
	PasswordDB = getPasswordDB()
	conn = connectDB(sys.PasswordDB[0])
	cursor = conn.cursor()
	companyNames = sys.argv[1:]
	print(companyNames)
	return
		# prepDB(conn, cursor, tableName)
	createSchema(conn, cursor, companyNames)
	for i in range(2, len(sys.argv)):
		tableName = sys.argv[i]
		prepDB(conn, cursor, tableName)

if __name__ == '__main__':
	main()