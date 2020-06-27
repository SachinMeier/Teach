
def read_data_naive(filename):
	""" 
	this function takes a file such as scores.txt and turns it into
	a list of lists of each person's scores. 
	scores = [ [P1's scores], [P2's scores], ...]
	Python will read all numbers in as strings, so we must individually
	convert each to an integer 
	"""
	with open(filename, "r") as fp:
		#data is now a list strings of each line
		data = fp.readlines()
	#print(data)
	# create an empty list
	scores = []
	# each line is a person's scores
	for s in data: # s is a single string of numbers
		# split each line along the spaces, now list 1 should =
		# ['94', '73', '72', '88', '75', '62', '92', '74', '99']
		string_list = s.split(" ")
		#print(string_list)
		# an empty list, reused each time
		person = []
		for t in string_list: # t is the string '94', then '73'...
			person.append(int(t)) # make t an int
		# add the person's scores list to the scores list
		scores.append(person) 
	return scores
"""
since s.split(" ") returns a full list, we can use it in the for loop
"""
def read_data_better(filename):
	with open(filename, "r") as fp:
		#data is now a list strings of each line
		data = fp.readlines()
	scores = []
	for s in data: 
		person = []
		for t in s.split(" "): # a for loop with 1 command is lame. 2 lines for 1 command??
			person.append(int(t))
		scores.append(person) 
	return scores
def read_data_efficient(filename):
	with open(filename, "r") as fp:
		data = fp.readlines()
	scores = []
	for s in data:
		# this line uses an in-line for loop. it just saves space. it does the a
		scores.append([int(t) for t in s.split(" ")])
	return scores
def read_data_wicked_fast(filename):
	with open(filename, "r") as fp:
		data = fp.readlines()
	# DOUBLE IN-LINE FOR LOOP!!!!
	scores = [[int(t) for t in s.split(" ")] for s in data]
	return scores

def read_people(filename):
	with open(filename, "r") as fp:
		data = fp.readlines()
	people = []
	for person in data:
		person = person.split(" ")
		people.append( [person[0], int(person[1])] )
	return people



def get_student_avgs():
	scores = read_data_wicked_fast("scores.txt")
	avgs = []
	for person in scores:
		avg = sum(person) / len(person) 
		avgs.append(avg)
	return avgs

def get_test_avg():
	scores = read_data_wicked_fast("scores.txt")
	student_count = len(scores)
	tests_count = len(scores[0])
	tests = []
	for t in range(tests_count):
		testSum = 0
		for s in scores:
			testSum += s[t]
		tests.append(testSum/student_count)
	return tests

if __name__ == "__main__":
	print(read_people("Files/people.txt"))
		

