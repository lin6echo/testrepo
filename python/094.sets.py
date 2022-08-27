thisset1 = set(("apple", "banana", "kiwi"))
print(thisset1)

thisset4 = {"banana", "cherry", "kiwi"}
thisset4.add("orange")
print(thisset4)

thisset5 = {"pear", "apple", "melon"}
tropical = {"kiwi", "mango", "pineapple"}
thisset5.update(tropical)
print(thisset5)  

thisset8 = {"apple", "kiwi", "pear"}
x = thisset8.pop()
print(x)
print(thisset8)

set1 = {"apple", "banana", "kiwi"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set4 = {"apple", "banana", "kiwi"}
set5 = {1, 2, 3}
set4.update(set5)
print(set4)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x) 

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
