import psycopg2

conn_string = "host='localhost' dbname='postgres' user='postgres'"


# print the connection string we will use to connect
print "Connecting to database\n	->%s" % (conn_string)

# get a connection, if a connect cannot be made an exception will be raised here
conn = psycopg2.connect(conn_string)

# conn.cursor will return a cursor object, you can use this cursor to perform queries
cursor = conn.cursor()
print "Connected!\n"

cursor.execute("INSERT INTO stock_data.symbols(symbol) values ('AAPL')")
conn.commit()
