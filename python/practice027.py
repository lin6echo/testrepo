thislist = ["apple", "banana", "kiwi", "pear", "orange"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

fruits = ["apple", "banana", "kiwi", "pear", "orange"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

sortedlist = [10, 12, 356, 99, 77, 1, 23]
sortedlist.sort()
print(sortedlist)

number = -20
absolute_number = abs(number)
print(absolute_number)