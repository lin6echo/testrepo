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
