list2 = [1, 2, 3, 4, 5, 6, 7,]
i = 0
while i < len(list2):
    print(list2[i])
    i = i + 1

list3 = [1, 2, 3, 4]
[print(x) for x in list3]

fruits = ["apple", "banana", "cherry"]
newlist = []
for x in fruits:
    newlist.append(x)

print(newlist)

fruits1 = ["apple", "banana", "cherry"]
newlist = [x for x in fruits1 if 'a' in x]
print(newlist)
