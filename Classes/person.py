"""
a Class can be considered like a data-type. 
Python is an Object-Oriented language, meaning most programs
create and manipulate objects. A class is a framework for an object.
An object is an instance of a class, like I am an instance of a Human

classes usually are capitalized, but the same naming rules apply like
with variables and functions: [a-z, A-Z, _, 0-9]

BUILD A CLASS:

class NAME(INHERITANCE):
	functions and variables

class is the keyword to start a class. 
NAME is the name.
we will cover INHERITANCE LATER, but for now, leave this blank and 
skip the parantheses. 

CLass Functions:
all class functions should have "self" as the first argument.

all classes should have a function called __init__(self, ARGS). init stands for initialize.
this is the function that executes the creation of an instance/object.
It initializes an instance of the class.


"""

class Person:
	"""
	a class for storing a Person's name and age.
	"""
	def __init__(self, name, age):
		"""
		arguments passed can be tied to the object by making them 
		object-specific variables. object-specific variables start
		with self.NAME, and are stored in memory outside of all 
		functions. They can be accessed directly.

		__init__ functions typically perform error checking as well
		"""
		# self.name is an object variable
		self.name = name
		#error checking
		if age < 0:
			# the raise keyword is how our programs can raise errors
			raise ValueError("Age cannot be negative")
		self.age = age

	def __repr__(self):
		"""
		the __repr__ function gets called when you print an object. You get to define
		what print(person) does. __repr__ should always return a string.
		"""
		return f"Name: {self.name}\nAge: {self.age}"

	def get_name(self):
		""" returns the person's name """
		return self.name

"""
Now, we can instantiate the Person class by creating a Person!
"""
# alex = Person("Alex", 18)
# print(alex)

"""
INHERITANCE:
a class can be derived from another class, so that it encompasses all of 
its parent's traits, as well as additional ones

ie. All Students are people, but not all people are students, so the student
class should inherit from Person, because all Students have a name and age.

we inherit by including the parent class in parantheses.
"""

class Student(Person):
	
	def __init__(self, name, age, year=1, gpas=[], clubs=[]):
		# We pass the appropriate variables to "super()" which 
		# is the parent class (Person). Student handles the gpas and clubs
		super().__init__(name, age) # Creates a Person
		# year should be an integer
		self.year = year
		# gpas is a list of doubles (number with decimal)
		self.gpas = gpas
		# clubs is a list of strings
		self.clubs = clubs

	def __repr__(self):
		"""
		even though Person has defined __repr__, we can overrule that, or any function
		by redefining it in the child/derived class.
		"""
		if self.year == 1:
			grade = "Freshman"
		elif self.year == 2:
			grade = "Sophomore"
		elif self.year == 3:
			grade = "Junior"
		elif self.year == 4:
			grade = "Senior"
		else:
			grade = "Graduated"
		return f"Student:\nName: {self.name}\nAge: {self.age}\nYear: {grade}"
	
	def update_gpa(self, newGPA):
		"""
		add a new Gpa to the list of GPAs.
		"""
		raise NotImplementedError("Not Implemented")

	def calculate_gpa(self):
		"""
		calculate the average of all GPAs in self.gpas
		"""
		raise NotImplementedError("Not Implemented")

	def add_club(self, club):
		"""
		add a new Club to the list of Clubs.
		"""
		raise NotImplementedError("Not Implemented")