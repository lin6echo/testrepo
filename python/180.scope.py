x = 50

def func():
    global x
    x = 100

print("before function call, x is: ", x)                # return: 50

func()

print("after function call, x is: ", x)                 # return: 100

# another way whitout global

x = 50

def func():
    x = 100
    return x

print("before function call, x is: ", x)                # return: 50

x = func()

print("after function call, x is: ", x)                 # return: 100