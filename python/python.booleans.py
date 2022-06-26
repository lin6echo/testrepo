# In programming you often need to know if an expression is True or False.

# You can evaluate any expression in Python, and get one of two answers, True or False.

# When you compare two values, the expression is evaluated and Python returns the Boolean answer:

# ------------------------------------------------------------------------------------------------------

print(10 > 9)
print(10 == 9)
print(10 < 9)

# ------------------------------------------------------------------------------------------------------

a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# ------------------------------------------------------------------------------------------------------

# Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))

# -------------------------------------------------------------------------------------------------------

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# -------------------------------------------------------------------------------------------------------

# Most Values are True

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# ---------------------------------------------------------------------------------------------------------

# Some Values are False
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# ---------------------------------------------------------------------------------------------------------------

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))      # One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:

# ---------------------------------------------------------------------------------------------------------------

# Functions can Return a Boolean
# You can create functions that returns a Boolean Value:

def myFunction() :
  return True

print(myFunction())

# -----------------------------------------------------------------------------------------------------------------

def myFunction() :      # Print "YES!" if the function returns True, otherwise print "NO!":
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

  # --------------------------------------------------------------------------------------------------------------

# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))













