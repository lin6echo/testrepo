# Dictionaries are used to store data values in key:value pairs.
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : "1964",
    "colors" : ["red", "white", "blue"]
}

print(thisdict)
print(thisdict["brand"])
print(type(thisdict))

# You can access the items of a dictionary by referring to its key name, inside square brackets:
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict["year"])
# There is also a method called get() that will give you the same result:
x = thisdict.get("model")
print(x)
