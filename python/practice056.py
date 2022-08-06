# Return Values
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement
def myfunction():
    pass

# Recursion
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Results")
tri_recursion(6)

# A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10
print(x(5))

# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))