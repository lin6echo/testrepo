# And (The and keyword is a logical operator)
a = 200
b = 30
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or (The or keyword is a logical operator)
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of conditions is True")

# nested if statements
x = 41
if x > 10:
    print("above 10")
if x > 20:
    print("and also above 20!")
else:
    print("but not above 20.")
