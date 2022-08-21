def func(x):
    return x**2

call = func(5)
print(call)

def func(x=2):
    return x**2

call = func()
print(call)

def func(word, freq):
    print(word*freq)
    
call = func('Csaba', 5)
print(call)

def func(word, freq = 1):
    print(word*freq)
    
call = func('Csaba', 10)
print(call)

def func(word, add = 5, freq = 1):
    print(word*(freq + add))
    
func('Csaba')


def my_function():
      print("Hello from a function")

my_function()