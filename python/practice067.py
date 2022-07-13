def myfunc(a = "bad"):
    print("Python is " + a) 
myfunc(a = "awesome")

x = abs(-7.25)

print(x)

dict = {
        "Csaba":"Szilvi",
        "Márk":"Zsani",
        "Peti":"Bogi",

    }
print(dict)

myset = {"alma", 12, True}
print(myset)

a = "Hello World"
print(a[1])

for x in "banana":
    print(x)

b = "Hello World" 
print(b[2:5])   

total = 0
for number in range(1,11):
     if number % 2 == 0:
         total += number
print(total)

n = 0
while n < 10:
     n += 1
     print(n)

for num in range(0, 10):
    if num % 2 == 1:
        print(num)


thislist = ["apple", "banana", "kiwi", "pear", "orange"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

fruits = ["apple", "banana", "kiwi", "pear", "orange"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

sortedlist = [10, 12, 356, 99, 77, 1, 23]
sortedlist.sort()
print(sortedlist)

number = -20
absolute_number = abs(number)
print(absolute_number)

x = "alma"
print(x.capitalize())

a = "Banán"
print(a.casefold())

x = 5
y = "John"
print(type(x))
print(type(y))

x, y, z = "Orange", "Banana", "Mandarin"
print(x)
print(y)
print(z)

import random
print(random.randrange(1,5))

a = "Hello World"
print(len(a))

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

txt = "The best thing in life are free!"
print("free" in txt)

txt1 = "The best thing in life are free!"
if "free" in txt1:
    print("Yes, 'free' is present." )

b = "HelloWorld"
print(b[1:6])
print(b.split(","))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
