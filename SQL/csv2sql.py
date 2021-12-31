import csv
import sqlutil

def parse_csv_file(filename):
	""" the parse file takes a string variable called filename
			and reads it as a list of CSV lines. 
  :param filename: the csv file to read
  :return: array (list of lists of values)
	"""
	# open the csv file
	with open(filename, newline='') as csvfile:
		# read each line where each value is separated by delimiter (comma)
		rd = csv.reader(csvfile, delimiter=',', quotechar='"')
		
		# first line of file is the column titles
		# we want to ignore it
		next(rd)
  
		# we are going to manipulate the data in the file
		# this data list is going to be the new list of lines
		data = []
  
  	# csv is all strings. we want to convert
		# year -> int
		# age group -> (int, int)
		# race can stay as a string
		# birth rate -> float (decimal)
		for row in rd:
			try:
				# convert year to int
				year = int(row[0])
				# age is a string "age1-age2 years". We need to split these up
				# into two strings
				age_min, age_max = row[1].split("-")
				# then convert both strings to ints
				age_min = int(age_min)
				# remove "years" from the end of the second string
				age_max = int(age_max.split(" ")[0])
				# no conversion necessary for race
				race = row[2]
				# convert birth rate to decimal
				print("(", row[3].strip(),")", sep="")
				birth_rate = float(row[3].strip())
				# add this row of data to our new data list
				data.append([year, age_min, age_max, race, birth_rate])
			except:
				continue
		# after all lines have been manipulated, 
		# return the cleaned data
		return data

def create_birth_rates_table(conn):
  query = '''
		CREATE TABLE IF NOT EXISTS births (
			id integer PRIMARY KEY,
			year int,
			age_min int,
			age_max int,
			race text,
			birth_rate decimal(4,2)
		)
  '''
  cur = conn.cursor()
  cur.execute(query)
  conn.commit()

def insert_row(conn, row):
  # this is the SQL query to insert a new row
  query = '''
		INSERT INTO births (year, age_min, age_max, race, birth_rate)
		VALUES($1,$2,$3,$4,$5)
  '''
  # ignore this
  cur = conn.cursor()
  # row contains: 		year		age_min	age_max	race	birth_ate
  cur.execute(query, (row[0], row[1], row[2], row[3], row[4]))
  conn.commit()
  

  
if __name__ == "__main__":
  # read data from csv file
	data = parse_csv_file("births.csv")
	# create connection to database file
	conn = sqlutil.create_connection("births.db")
	# create a table within the database
	create_birth_rates_table(conn)
	# insert every row of data into the new table
	for row in data:
		insert_row(conn, row)
  