fruits = ["banana", "apple", "strawberry"]

for fruit in fruits:
    print(fruit)
    
[print(fruit) for fruit in fruits]

new_fruits = []
for fruit in fruits:
    fruit = fruit.upper()
    new_fruits.append(fruit)
    
fruits = new_fruits
print(fruits)