import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import json

x = {
        "name":"John",
        "age":30,
        "married":True,
        "divorced":False,
        "children":("Ann", "Billy"),
        "pets":None,
        "cars":[
            {"model":"BMW 230", "mpg":27.5},
            {"model":"Ford Edge", "mpg":24.1}
        ]
    }

print(json.dumps(x))

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))

json.dumps(x, indent=4, sort_keys=True)

    #RegEx Module

    #Python has a built-in package called re, which can be used to work with Regular Expression.

import re

    #Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
            print("YES! We have a match!")
else:
            print("No match")
            
import re
    
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)     