fruits = ["banana", "orange", "kiwi", "apple", "pear"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

thislist = ["banana", "orange", "kiwi", "apple", "pear"]
thislist.sort()
print(thislist)