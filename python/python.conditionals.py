# IF
    # This is the basic syntax to test if a condition is true.
    # If so, the indented code will be executed, if not it will be skipped.
from asyncio import TimerHandle


n = 3
if n > 2:
    print("Larger than 2")

# ELSE
    # This is a way to specify some code that will be executed if a condition is false.
age = 11
if age > 16:
    print("Can drive")
else:
    print("Don't drive")

# ELIF
    # In addition to the initial if statement condition, you can add extra conditions to test if the first condition is false.
    # Once an elif condition is true, the rest of the elif conditions are no longer checked and are skipped.
weather = "sunny"
if weather == "rain":
    print("bring umbrella")
elif weather == "sunny":
    print("bring sunglasses")
elif weather == "snow":
    print("bring gloves")

# AND
    # This expects both conditions either side of the and to be true.
s = 58
if s < 60 and s > 50:
    print("Your grade is C")

# OR
    # This expects either of the conditions either side of the or to be true. Basically, both conditions cannot be false.
age = 12
if age < 16 or age > 200:
    print("Can't drive")

# NOT
    # This will flip the original result of the condition. e.g. if it was true then it's now false.
if not 3 > 1:
    print("something") # Will not be printed

# COMPARISON OPERATORS
    # These mathematical comparison operators allow you to refine your conditional checks.
"> Greater than"
"< Lesser than"
">= Greater than or equal to"
"<= Lesser than or equal to"
"== Is equal to"
"!= Is not equal to"