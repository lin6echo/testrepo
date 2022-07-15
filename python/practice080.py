import datetime

x = datetime.datetime(2022, 7, 15)

print(x)

import datetime

x = datetime.datetime(2022, 7, 15)

print(x.strftime("%B"))

x = min(5,10,25)
y = max(5,10,25)

print(x)
print(y)

x = abs(-7.25)
print(x)

x = pow(4,3)
print(x)

import math

x = math.sqrt(64)
print(x)

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x)
print(y)

import math

x = math.pi

print(x)

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

import json

    # a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

    # convert into JSON:
y = json.dumps(x)

    # the result is a JSON string:
print(y)

    