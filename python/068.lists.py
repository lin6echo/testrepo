list = ["apple", "pear", "kiwi", "cherry"]
list.insert(2, "orange")
print(list)

list1 = ["apple", "pear", "kiwi", "cherry"]
list1.append("melon")
print(list1)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

list = ['apple', 'banana', 'cherry']
tuple = ("kiwi", "orange")
list.extend(tuple)
print(list)

list = ["apple", "banana", "cherry"]
list.remove("banana")
print(list)


list1 = ["apple", "banana", "cherry"]
list1.pop(0)
print(list1)

for x in list:
    print(x)

list1 = ["apple", "banana", "pear"]
for i in range(len(list1)):
    print(list1[i])
