mydict = {"name" : "Max", "age" : 28, "city" : "Boston"}
print(mydict)
print(type(mydict))

mydict2 = dict(name="Mary", age=26, city="London")
print(mydict2)
print(type(mydict2))

value = mydict["name"]
print(value)

# mydict["email"] = "max@xyz.com"
# print(mydict)

# del mydict["name"]
# print(mydict)

# mydict.pop("age")
# print(mydict)

# mydict.popitem()
# print(mydict)

if "name" in mydict:
    print("yes")
else:
    print("no")
    
try:
    print(mydict["name"])
except:
    print("error")
    
for key in mydict:
    print(key)
# same
for key in mydict.keys():
    print(key)
    
for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

mydict_cpy = mydict
print(mydict_cpy)

# mydict_cpy["email"] = "max@xyz.com"
# print(mydict_cpy)
# print(mydict)

mydict_cpy = mydict.copy()
print(mydict_cpy)

mydict_cpy = dict(mydict)

mydict_cpy["email"] = "max@xyz.com"
print(mydict_cpy)
print(mydict)

mydict = {"name" : "Max", "age" : 28, "email" : "max@xyz.com"}
mydict2 = dict(name="Mary", age=27, city="Budapest")

mydict.update(mydict2)
print(mydict)

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

value = my_dict[3]
print(value)

my_tuple = (8, 7)
my_dict = {my_tuple: 15}
print(my_dict)






