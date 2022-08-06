#  RANGE
    # Often you will want to generate a range of numbers. You can specify the start, end and step.
    # Start is included, but end is excluded: start >= range < end
#range(start, end, step)
for i in range(6, 0, -2):
    print(i) # result: 6, 4, 2,
             # 0 is not included.

# RANDOMISATION
    # The random functions come from the random module which needs to be imported.
    #In this case, the start and end are both included.
    # start <= randint <= end
    import random
    # randint(start, end)
    n = random.randint(2, 5)
    print(n)
    # n can be 2, 3, 4, or 5.

# ROUND
    # This does a mathematical round. So 3.1 becomes 3, 4.5 becomes 5, and 5.8 becomes 6.
print(round(4.6))
# result 5

# ABS
    # This returns the absolute value. Basically removing any -ve signs.
print(abs(-4.6))
# result 4.6