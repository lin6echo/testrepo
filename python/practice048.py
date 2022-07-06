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

# The keys() method will return a list of all the keys in the dictionary.
y = thisdict.keys()
print(y)

# The values() method will return a list of all the values in the dictionary.
z = thisdict.values()
print(z)

# The items() method will return each item in a dictionary, as tuples in a list.
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

# 
thisdict["color"] = "red"
print(thisdict)

thisdict.update({"color": "green"})
print(thisdict)

# The pop() method removes the item with the specified key name:
thisdict.pop("model")
print(thisdict)