# INTEGERS
# Integers are whole numbers.
my_number = 354

# FLOATING POINT NUMBERS
# Floats are numbers with decimal places. When you do a calculation that results in a fraction e.g. 4 / 3 the result will always be
# a floating point number.
my_float = 3.14159

# STRINS
# A string is just a string of characters. It should be surrounded by double quotes.
my_string = "Hello"

# STRING CONCATENATION
# You can add strings to string to create a new string. This is called concatenation. It results in a new string.
concatenate = "Hello" + "Angela"
print(concatenate) # becomes "HelloAngela"

# ESCAPING A STRING
# Because the double quotes is special, it denotes a string, if you want to use it in a string, you need to escape it with a "\"
speech = "She said: \"Hi\""
print(speech) # prints: She said: "Hi"

# F-STRING
# You can insert a variable into a string using f-string.
# The syntax is simple, just insert the variable in-between a set of curly bracers {}.
days = 365
print(f"There are {days} in a year")

# CONVERTING DATA TYPES
# You can convert a variable from 1 data type another.
# Converting to float: float()
# Converting to int: int()
# Converting to string: str()
n = 354
new_n = float(n)
print(new_n) # result 354.0

# CHECKING DATA TYPES
# You can use the type() function to check what is the data type of a particular variable.
n = 3.14159
print(type(n)) # result float