adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x,y)
        
def my_function():
    print("Hello from my function.")

my_function()

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1="Emil", child2="Tobias", child3="Linus")

def my_function(country="Hungary"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

def myfunc1(q = "bad"):
    q = "awesome"
    print("Python is " + q)

myfunc1()

x = "awesome"

def myfunc2():
    global x
    x = "fantastic"

myfunc2()
print("Python is " + x)

