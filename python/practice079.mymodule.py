import mymodule
mymodule.greeting("Csaba")

import mymodule1

a = mymodule1.person1["age"]

print(a)

import mymodule1 as mx

a = mx.person1["age"]
print(a)

import platform

x = platform.system()
print(x)

import platform

x = dir(platform)
print(x)

def greeting(name):
    print("Hello, " + name)

person1 = {
    "name" : "Csaba",
    "age" : 57,
    "country" : "Hungary"
}

from mymodule1 import person1

print(person1["age"])

import datetime

x = datetime.datetime.now()
print(x)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))