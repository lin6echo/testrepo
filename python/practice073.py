thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
y = thisdict.keys()
print(y)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
z = thisdict.values()
print(z)

b = thisdict.items()
print(b)

thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary.")

thisdict["year"] = 2018
print(thisdict)


# The update() method will update the dictionary with the items from the given argument.
thisdict.update({"year": 2020})
print(thisdict)

thisdict["color"] = "red"
print(thisdict)

thisdict.update({"color": "green"})
print(thisdict)

thisdict.pop("model")
print(thisdict) 

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
for x in thisdict:
        print(x)

# Print all values in the dictionary, one by one:
for x in thisdict:
    print(thisdict[x])

# You can also use the values() method to return values of a dictionary:
for x in thisdict.values():
    print(x)

# You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
    print(x)

for x, y in thisdict.items():
    print(x,y)

# Make a copy of a dictionary with the copy() method:
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict = thisdict.copy()
print(mydict)

