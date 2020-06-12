


# These are comments. Single line comments start with #
"""
Multi-line comments start and end with triple quotes (single or double)
They can be any length.
Place multipline comments under a function definition to document it.
"""


# Here is a string variable. Create variables by 
# naming them and then assigning them using '=' and the value
# a string can be started and ended with single or double quotes
# variables can be named with alphanumerics and _ (underscore). Cannot begin with a number 
word = "hello world" 
# here is a number variable
x = 5
# a Boolean (bool) variable can be either True of False (capital)
yes = True 
no = False

# complex var types:
# list starts with brackets []
# can contain any data type
list_int = [0, 1, 2, 4, 5]
list_str = ["hello", "world", "goodbye"]
list_bool = [True, False, True, True]
# lists can be accessed by index, which STARTS AT 0
# so first element is index 0, second = 1...last = size - 1
list_int[0] = 3
# list_int is now = [3,1,2,4,5]
print(list_int[2]) # prints 2


# Dictionaries
# start with curly braces {}
# contain a key and a value. such that key: value
dictionary = {
	"apple": "red",
	"banana": "yellow",
	"grape": "purple",
	"mango": ["green", "yellow", "red"]
}
# dictionary can be accessed by key, and returns value
dictionary["apple"] = "green"

print(dictionary["banana"]) # prints "yellow"


# if Statements follow this format:
# if ( STATEMENT ):
#  [TAB] COMMANDS
# 
# STATEMENT must evaluate to a boolean (true or false) value. 
# nonzero Numbers are always true
# strings are true if non-empty
# >, <, ==, <=, >=, are all comparison operattors that yield true or false

# Indents are absolutely necessary in python
# COMMANDS can be any number of lines of normal python code, including additional ifs, loops, 
# these commands will only be executed if the STATEMENT is true.

if yes: # True always evaluates to true, so COMMANDS will execute
	print("yes")
if no: # False always false, so COMMANDS doesnt execute
	print("no") # never prints
if x == 5: # to evaluate if 2 objects are equal, use  ==. 
	print("x == 5")
if x > 6:
	print("x > 6")

# after an if, you can add an 'elif' statement, (else if), 
# which acts as an if statement only if the previous if statement
# is false. any number of elifs can be appended.
# lastly, an else statement can end a block of if/elifs. 

# only 1 if
if x < 4: 
	print("x < 4")
elif x > 4: #else if -> elif
	print("x > 4")
elif x == 5:
	print("x = 5")
# any number of elifs
#only one else
else:
	print("x = 4")

if ((x == 5) or not yes) and not no:
	print("at least one is true")
"""
LOOPS: 
	loops are blocks of code that are executed repeatedly. Each time through the list of commands in
	the block is called an iteration
	- for i in (ITER):
		COMMANDS
	inside the 'for' block, i = each item in the ITER 
	ITER is an iterable, such as a list, or string. 
	In a string, each letter is an item.

	- for i in range(y):
		COMMANDS

	each iteration, i is an integer, starting at 0 and ending at y-1

	- for i in range(x, y, z):
	each iteration, i is an integer starting at x, ending at y-1, and incrementing by z each iteration

	- for i, n in enumerate(ITER):
		COMMANDS

	each iteration, i is an index of the items in the ITER. while x is the item. i is essentially a count 
	of the iterations, STARTING at ZERO
	- while (STATEMENT):
		COMMANDS
"""
for x in list_int:
	print(x) # prints 3 then 1 then 2 4 5

for i, x in enumerate(list_str):
	print(i, ":", x) #prints "0: Hello", then "1: World", then "2: Goodbye"


while (yes):
	print("s")
	print("a")
	print("d")
	print("f")
	print("g")
	break



"""
Recursive Function

"""
def myfunc(y):
	y += 1
	if y < 9:
		myfunc(y)
	print(y)


""" 
Working with strings
"""
gender = False
greeting = "hello"
name = "Sachin"
m = "male"
f = "female"
age = 19
#Inefficient way (with error: Can't add int to string)
#message = greeting + " " + name + ". You are " + age + "years old."

'''
Better way: use f"words {variable or logic}"
alternative:
"words {}, {}".format(var1, var2)

'''
message = f"{greeting} {name}. You are {age*12} months old."
msg2 = "{} {}. You are {} months old".format(greeting, name, age*12)
print(message)

# STRING INDEXING
'''
Strings can be indexed like lists

string[x:y:z]
x = start point (inclusive)
y = end point (non-inclusive)
z = interval (default =1, -1 = backwards)
any of the positions can be left blank
'''
greeting[0] # = "h"
greeting[:3] # = "hel"
greeting[1:3] # = "el" note: doesnt include the second l (index [3])
greeting[1:] # = "ello"
greeting[0:3:2] # = "hl" prints every other letter: 0,2
greeting[::-1] # = "olleh", start and end left blank
greeting[-1] # = "o" negative indeces start with -1 = last element, -2 = second to last...
greeting[1:-2] # = "el" negative indeces can be used with positive ones.