from person import Person, Student

"""
Instantiating a class works exactly like declaring a variable,
but the Class should have parantheses after, including all 
arguments passed to __init__
"""
alice = Person("Alice", 18)
bob = Person("Bob", 19)
dave = Student("Dave", 18, year=2, gpas=[3.4, 3.54, 3.62, 3.76], clubs=["chess", "mock trial"])

# print(alice.get_name()) # A Person has the function get_name
# print(bob.get_name()) # A Student is a Person, so it also has get_name

print(alice) # uses Person.__repr__()
print(dave)

# charlie = Student("Charlie", 20, year=2)

# print(charlie.get_year())