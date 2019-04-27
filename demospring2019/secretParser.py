def getSecret():
	"""
	parses credentials.json and allows other program files to access database password for user 'rcos' to create tables/schemas

	Returns:
	list of size 1 containing password for user 'rcos' in database

	"""
	f = open("secret.txt", 'r')
	return (f.read().split('\n'))
	

