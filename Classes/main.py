from person import Person, Student, Book

"""
Instantiating a class works exactly like declaring a variable,
but the Class should have parantheses after, including all 
arguments passed to __init__
"""

if __name__ == "__main__":
    md = Book(1, "Moby Dick", "Herman Melville", 1755)

    sachin = Student("sachin", 20, 3)

    sachin.check_out_book(md)
    print(sachin.books)