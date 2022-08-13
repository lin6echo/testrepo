mylist = ["banana", "cherry", "lemon"]
print(mylist)

for x in mylist:
    print(x)

if "banana" in mylist:
    print("yes")
else:
    print("no")
    
item = mylist[1]
print(item)

print(len(mylist))

mylist.append("kiwi")
print(mylist)

mylist.insert(1, "apple")
print(mylist)

item1 = mylist.pop()
print(item1)
print(mylist)

item2 = mylist.remove("cherry")
print(mylist)

item = mylist.reverse()
print(mylist)

# item3 = mylist.clear()
# print(mylist)

item = mylist.sort()
print(mylist)

my_list1 = [1, 3, 7, 2, -7, -3, -10]
print(my_list1)

new_list = sorted(my_list1)
print(my_list1)
print(new_list)

mylist2 = [0] * 5
print(mylist2)

mylist3 = [1, 2, 3, 4, 5]

newlist = mylist2 + mylist3
print(newlist)

mylist4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = mylist4[1:5]
print(a)

b = mylist4[::2]
print(b)

c = mylist4[::-1]
print(c)

list_org = ["banana", "kiwi", "apple"]
# list_cpy = list_org
# list_cpy = list_org.copy()
# list_cpy = list(list_org)
list_cpy = list_org[:]
list_cpy.append("lemon")
print(list_cpy)
print(list_org)

a1 = [1, 2, 3, 4, 5, 6]
b1 = [i*i for i in a1]

print(a1)
print(b1)

