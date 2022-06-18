# CREATING FUNCTION
    # This is the basic syntax for a function in Python. It allows you to give a set of instructions a name,
    # so you can trigger it multiple times without having to re-write or copy-paste it.
    # The contents of the function must be intended to signal that it's inside.
from tkinter import N


def my_function():
    print("Hello")
    name = input("Your name:")
    print("Hello")

# CALLING FUNCTION
    # You activate the function by calling it.
    # This is simply done by writinsg the name of the function followed by a set of round brackets.
    # This allows you to determine when to trigger the function and how many times.
my_function()
my_function()
    # The function my_function
    # will run twice

# FUNCTIONS WITH INPUT
    # In addition to simple functions, you can give the function can do something different depending on the input.
    # It makes your function more useful and re-usable.
def add(n1, n2):
    print(n1 + n2)
add(2, 3)

# FUNCTION WITH OUTPUTS
    # In addition to inputs, a function can also have an output. The output value is proceeded by the keyword "return".
    # This allows you to store the result from a function.
def add(n1, n2):
    return n1 + n2
result = add(2, 3)
print(result)

# VARIABLE SCOPE
    # Variable created inside a function are destroyed once the function has executed.
    # The location (line of code) that you use a variable will determine its value.
    # Here n is 2 but inside my_function() n is 3.
    # So printing n inside and outside the function will determine its value.
n = 2
def my_function():
    n = 3
    print(n)
print(n) # prints 2
my_function() # prints 3

# KEYWORD ARGUMENTS
    # When calling a function, you can provide a keyword argument or simply just the value.
    # Using a keyword argument means that you dont't have to follow any order when providing the inputs.
def divide(n1, n2):
    result = n1 / n2
# Option 1:
divide(10, 5)
# Option 2:
divide(n2 = 5, n1 = 10)
