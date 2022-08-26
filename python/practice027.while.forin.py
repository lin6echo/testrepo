thislist = ["apple", "banana", "kiwi", "pear", "orange"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

fruits = ["apple", "banana", "kiwi", "pear", "orange"]
newlist = []

for x in fruits:
    if "p" in x:
        newlist.append(x)

print(newlist)
