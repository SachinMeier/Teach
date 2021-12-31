import sqlutil

def avg_birth_rate(conn):
	query = '''
		SELECT avg(birth_rate)
		FROM births
	'''
	rows = sqlutil.select(conn, query)
	sqlutil.display_rows(rows)

def avg_birth_rate_for_race(conn, race):
	query = '''
		SELECT race, avg(birth_rate)
		FROM births
		WHERE race=?
  '''
	rows = sqlutil.select(conn, query, (race,))
	sqlutil.display_rows(rows)
  
def avg_birth_rates_by_year(conn):
  query = '''
		SELECT distinct(year), avg(birth_rate)
		FROM births
		GROUP BY year
  	ORDER BY year ASC
  '''
  rows = sqlutil.select(conn, query)
  sqlutil.display_rows(rows)

if __name__ == "__main__":
  conn = sqlutil.create_connection("births.db")
  # avg_birth_rate_for_race(conn, "All Races")
  # avg_birth_rate(conn)
  avg_birth_rates_by_year(conn)
  