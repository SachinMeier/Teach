from ex import (
	read_data_wicked_fast, 
	read_people
)

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

	def get_age(self):
		""" return the person's age """
		return self.age

	def get_months(self):
		return self.age * 12


def list_people():
	data = read_people("Files/people.txt")
	people = []
	for p in data:
		person = Person(p[0], p[1])
		people.append(person)
	print(people)

if __name__ == "__main__":
	list_people()