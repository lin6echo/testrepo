thisset = {"apple", "banana", "cherry"}
print(thisset)

# Set items are unordered, unchangeable, and do not allow duplicate values

thisset = {"apple", "banana", "cherry"}
print(len(thisset))

thisset1 = set(("apple", "banana", "kiwi"))
print(thisset1)                                 # It is also possible to use the set() constructor to make a set.

thisset2 = {"apple", "banana", "cherry"}
for x in thisset2:
    print(x)

thisset3 = {"apple", "banana", "cherry"}
print("banana" in thisset3)

thisset4 = {"banana", "cherry", "kiwi"}
thisset4.add("orange")
print(thisset4)                             # To add one item to a set use the add() method.

thisset5 = {"pear", "apple", "melon"}
tropical = {"kiwi", "mango", "pineapple"}
thisset5.update(tropical)
print(thisset5)                             # To add items from another set into the current set, use the update() method.

thisset6 = {"apple", "banana", "cherry"}
myset = ["kiwi", "orange"]
thisset6.update(myset)
print(thisset6)

thisset7 = {"apple", "banana", "cherry"}
thisset7.remove("apple")
print(thisset7)

thisset8 = {"apple", "kiwi", "pear"}
x = thisset8.pop()
print(x)
print(thisset8)                             # the pop() method to remove an item, but this method will remove the last item