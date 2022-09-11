# While loop
n = 1
while n < 100:
    n += 1
    print(n)

# For loop
all_fruits = ["apple", "banana", "kiwi"]
for fruit in all_fruits:
    print(fruit)

thistuple1 = ("apple", "banana", "cherry")
if "banana" in thistuple1:
    print("Yes")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

total = 0
for number in range(1,11):
     if number % 2 == 0:
         total += number
print(total)

n = 0
while n < 10:
     n += 1
     print(n)

for num in range(0, 10):
    if num % 2 == 1:
        print(num)

