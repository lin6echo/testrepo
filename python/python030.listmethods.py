# ADDING LISTS TOGETHER
    # You can extend a list with another list by using the extend keyword, or the + symbol.
list1 = [1, 2, 3]
list2 = [9, 8, 7]
new_list = list1 + list2
print(new_list)
list1 += list2

#---------------------------------------------------------------------------------------------------------------------

# ADDING AN ITEM TO A LIST
    # If you just want to add a single item to a list, you need to use the .append() method.
all_fruits = ["apple", "banana", "orange"]
all_fruits.append("pear")
print(all_fruits)

#--------------------------------------------------------------------------------------------------------------------

# LIST INDEX
    # To get hold of a particular item from a list you can use its index number.
    # This number can also be negative, if you want to start counting from the end of the list.
letters = ["a", "b", "c"]
print(letters[0])
letters[-1]
print(letters[-1])

#------------------------------------------------------------------------------------------------------------------------

# LIST SLICING
    # Using the list index and the colon symbol you can slice up a lit to get only the portion you want.
    # Start is included, but end is not.
# list[start:end]
letters = ["a", "b", "c", "d"]
letters[1:3]
print(letters[1:3])