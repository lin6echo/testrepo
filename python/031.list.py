b = "Hello World"
print(b[1:6])
print(b.split(","))
#------------------------------------------------------------------------
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#------------------------------------------------------------------------
mylist = ["apple", "mango", "pear"]
print(mylist)
print(len(mylist))
print(type(mylist))
#------------------------------------------------------------------------
thislist = list(("apple", "banana", "kiwi", "orange", "melon"))
print(thislist)
print(thislist[1])
print(thislist[2:5])
#------------------------------------------------------------------------
thislist1 = list(("apple", "banana", "kiwi", "orange", "melon"))
if "banana" in thislist1:
    print("Yes, 'banana' is in the list")

thislist2 = list(("apple", "banana", "kiwi", "orange", "melon"))
thislist2[1:3] = ["cherry", "mango"]
print(thislist2)
