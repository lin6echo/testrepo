# Creating a Function
def my_function():
    print("Hello from a function.")
my_function()

def my_function(fname):
    print(fname + "Refress")
my_function("Emil ")
my_function("Csaba ")
my_function("Márk ")

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes")

# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

# Keyword Arguments
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Default Parameter Value
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)