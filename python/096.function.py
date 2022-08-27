def myfunc(a = "bad"):
    print("Python is " + a) 
myfunc(a = "awesome")

def myfunc():
        x = "fantastic"
        print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
    global x 
    x = "fantastic"

myfunc()
print("Python is " + x)