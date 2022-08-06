def my_function():                  		# The def keyword is used to create, (or define) a function.
  print("Hello from a function")

my_function()

x = "awesome"

def myfunc():
    global x 
    x = "fantastic"

myfunc()
print("Python is " + x)

fruits = ["banana", "orange", "kiwi", "apple", "pear"]
newlist = []
for x in fruits:
        if "a" in x:
            newlist.append(x)

print(newlist)

mylist = ["apple", "pear", "peach"]
print(mylist)

x = len(mylist) 		# return: 3 -> The len() function returns the number of items in an object.
print(x)

name = "Fred"                           # A formatted string literal or f-string is a string
print(f"He said his name is {name}.")   

def my_function():                  		# The def keyword is used to create, (or define) a function.
    print("Hello from a function")

my_function()

total = 0
for number in range(1, 101):
    if number % 2 == 0:             	# Csak a páros számokat adja össze 1-100-ig
        total += number
print(total)

total1 = 0
for number in range(1, 101):
    total1 += number                		# Minden számot összead 1-100-if
print(total1)

x = "awesome"

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

import random

print(random.randrange(1,5))

x = "Hello World Ohio"
print(x[1:8])
print(x.upper())
print(x.lower())
print(x.strip())
print(x.replace("H", "J"))
print(x.split("o"))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

thislist = ["banana", "orange", "kiwi", "apple", "pear"]
thislist.sort()
print(thislist)

letters = ["a", "b", "c", "d"]
letters[1:3]
print(letters[1:3])

thistuple = ("apple", "banana", "cherry")

for x in thistuple:
    print(x)

for i in range(len(thistuple)):
    print(thistuple[i])

i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
x = Person("Csaba", "Bajzáth")
x.printname()

