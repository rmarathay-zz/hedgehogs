POSTGRES_USER = "rcos"
POSTGRES_PASSWORD = "hedgehogs_rcos"
DBNAME = "rcos"

# Use this host to connect to the remote PostgreSQL server
HOST = "206.189.181.163"    # Ranjit
#HOST = "192.168.99.100"    # Your local
PORT = "5432"

def make_conn_string():
    ret = "host={} port={} user={} password={} dbname={}"\
    .format(HOST, PORT, POSTGRES_USER, POSTGRES_PASSWORD, DBNAME)
    return ret
