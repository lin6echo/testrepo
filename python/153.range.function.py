#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), 
# and stops before a specified number.

x = range(6)
for n in x:
  print(n)

#Create a sequence of numbers from 3 to 5, and print each item in the sequence:

x = range(3, 6)
for n in x:
  print(n)

#Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:

x = range(3, 20, 2)
for n in x:
  print(n)

