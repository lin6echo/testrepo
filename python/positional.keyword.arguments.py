# Function with more than 1 input
# Positional argument
# First argument --- First parameter
# Second argument ---- Second parameter

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Csaba", "Eger")

# Function with keyword argument
# Keyword arguments
# my_function(c=3, a=1, b=2)

def greet_with_keyword(name="Csaba", location="Eger"):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with_keyword()
