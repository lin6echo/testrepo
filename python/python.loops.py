# WHILE LOOP
    # This is a loop that will keep repeating itself until the while condition becomes false.
n = 1
while n < 100:
    n += 1
    print(n)

# FOR LOOP
    # For loops give you more control than while loops. You can loop through anything that is iterable. e.g. a range, a list, 
    # a dictionary or tuple
all_fruits = ["apple", "banana", "orange"]
for fruit in all_fruits:
    print(fruit)

# _ IN A FOR LOOP
    # If the value your for loop is iterating through, e.g. the number in the range, or the item in the list is not needed,
    # you can replace it with an underscore.
"for _ in range(100):"
    # Do something 100 times.

# BREAK
    # This keywords allows you to break free of the loop. You can use it in a for or while loop.
scores = [34, 67, 99, 105]
for s in scores:
    if s > 100:
        print("invalid")
        break
    print(s)

# CONTINUE
    # This keyword allows you to skip this iteration of the loop and go to the next. 
    # The loop will still continue, but it will start from the top.
n = 1
while n < 100:
    if n % 2 == 0:
        continue
    print(n)
    # Prints all the odd numbers

# INFINITE LOOPS
    # Sometimes the condition you are checking to see if the loop should continue never becomes false.
    # In this case, the loop will continue for eternity (or until your computer stops it). 
    # This is more common with while loops.
while 5 > 1:
    print("I'm a survivor.")