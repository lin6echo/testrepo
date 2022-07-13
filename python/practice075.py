x = "awesome"

def my_func():
    print("Python is " + x)

my_func()
#--------------------------------------------
days = 365
print(f"There are {days} in a year.")
#--------------------------------------------
class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
p = Person('Nikhil')
p.say_hi()
#--------------------------------------------
class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
# Creating different objects
p1 = Person('Nikhil')
p2 = Person('Abhinav')
p3 = Person('Anshul')
 
p1.say_hi()
p2.say_hi()
p3.say_hi()
#----------------------------------------------
thistuple1 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple1.count(5)
print(x)

thistuple2 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple2.index(8)
print(x)

thisset1 = set(("apple", "banana", "kiwi"))
print(thisset1)

thisset4 = {"banana", "cherry", "kiwi"}
thisset4.add("orange")
print(thisset4)

thisset5 = {"pear", "apple", "melon"}
tropical = {"kiwi", "mango", "pineapple"}
thisset5.update(tropical)
print(thisset5)  

thisset8 = {"apple", "kiwi", "pear"}
x = thisset8.pop()
print(x)
print(thisset8)

set1 = {"apple", "banana", "kiwi"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set4 = {"apple", "banana", "kiwi"}
set5 = {1, 2, 3}
set4.update(set5)
print(set4)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True.")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True.")

x = 41
if x > 10:
    print("Above ten,")
if x > 20:
    print("and also above 20!")
else:
    print("but not above 50.") 

i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

fruits = ["banana", "apple", "cherry"]
for x in "banana":
    print(x)

for x in range(2,6):
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")