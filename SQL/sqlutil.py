import sqlite3

def create_connection(db_file):
	""" create a database connection to the SQLite database
	    specified by the db_file
	:param db_file: database file
	:return: Connection object or None
	"""
	return sqlite3.connect(db_file)
  
  
def select(conn, query, values=None):
	cur = conn.cursor()
	if values:
		cur.execute(query, values)
	else:
		cur.execute(query)
	return cur.fetchall()
  
def display_rows(rows):	
	for row in rows:
		print(row)
  
  