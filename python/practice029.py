x = 5
y = "John"
print(type(x))
print(type(y))

x, y, z = "Orange", "Banana", "Mandarin"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["Orange", "Banana", "Kiwi"]
x, y, z = fruits
print(x)
print(y)
print(z)

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
