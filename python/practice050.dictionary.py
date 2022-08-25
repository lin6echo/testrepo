# Make a copy of a dictionary with the copy() method:
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict().
mydict = dict(thisdict)
print(mydict)

child1 = {
"name" : "Emil",
"year" : 2004
}
child2 = {
"name" : "Tobias",
"year" : 2007
}
child3 = {
"name" : "Linus",
"year" : 2011
}
myfamily = {
"child1" : child1,
"child2" : child2,
"child3" : child3
}
print(myfamily)