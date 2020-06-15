"""
LOOPS: 
	loops are blocks of code that are executed repeatedly. Each time through the list of commands in
	the block is called an iteration
	

	- for i in range(x, y, z):
	each iteration, i is an integer starting at x, ending at y-1, and incrementing by z each iteration

	
	- while (STATEMENT):
		COMMANDS
"""
list_int = [3,1,2,4,5]
list_str = ["hello", "world", "goodbye"]
yes = True

def loop_for_1():
	"""
	- for i in (ITER):
		COMMANDS
	inside the 'for' block, i = each item in the ITER 
	ITER is an iterable, such as a list, or string. 
	In a string, each letter is an item.

	
	"""
	sum_of_list = 0
	for x in list_int:
		sum_of_list += x
		#print(x) # prints 3 then 1 then 2 4 5
	print(sum_of_list)

def loop_for_2():
	"""
	- for i, n in enumerate(ITER):
		COMMANDS

	each iteration, i is an index of the items in the ITER. while x is the item. i is essentially a count 
	of the iterations, STARTING at ZERO
	"""
	for i, x in enumerate(list_str):
		print(i, ":", x) #prints "0: Hello", then "1: World", then "2: Goodbye"

def loop_for_3():
	"""
	- for i in range(x, y, z):
		COMMANDS
	each iteration, i is an integer, starting at x and ending at y-1, interval z
	x = start point (inclusive, DEFAULT = 0)
	y = end (non-inclusive) (no default, must be specified)
	z = interval (DEFAULT = 1 )

	"""
	for i in range(10):
		print(i)
	for i in range(5, 15):
		print(i)
	for i in range(5, 15, 2):
		print(i)

def loop_while_1():
	"""
	A While loop executes an infinite number of times, so long as its condition is true:
	while (BOOL STATEMENT):
		COMMANDS

	the bool statement must evaluate to true. This can be a comparison (x > 5), a bool variable (yes)
	or a combination (x + 5 < 6 and x < 1)
	"""
	y = 5
	while (y > 0): # an infitite loop
		print("s")
		print("a")
		print("d")
		print("f")
		print("g")
		y -= 1 # this decrements y by 1 each time. y -= 1 is equivalent to y = y - 1
"""
Other loop keywords:

break: as seen in previous func, terminates the single most immediate loop

continue: terminates the single most immediate iteration. the loop starts from the top
"""
def loop_while_2():
	while True: # True is a value, not a variable. 
		print("s")
		print("a")
		break # break ends the most immediate loop, so it only executes once
		# if you comment this break statement out, it will print these letters infinitely
def loop_while_3():
	z = 10
	while z > 0:
		print("yes")
		continue	# continue causes the loop to restart from here. so it will nevver print no. 
		print("no")

"""
NESTING Loops

Loops can be placed inside loops as many times as needed.
Each loop still operates the same way. Interior loops go through fully 
for each time through the exterior loop.

"""
def nested_loop():
	a = "asdf"
	for y in range(4):
		print(y, end=' ') #prints i with no newline at the end, just a space.
		for letter in a:
			print(letter, end=' ') # prints each letter in the string a
		print("") # prints a newline

def nested_loop_2():
	"""
	prints a phone-like grid
	"""
	# list of 3 lists of 3 numbers. can be seen as 3x3 grid
	list_of_lists = [[1,2,3],[4,5,6],[7,8,9]] 
	for i in list_of_lists: # i will be each item in l_of_l, so i will be a list object
		for j in i: # j will be each item in i, an integer
			print(j, end=' ')
		print("") 

nested_loop_2()