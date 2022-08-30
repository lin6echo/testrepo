print(8 / 3) #/2.666666666666666666666
print(round(8 / 3)) #/3 (kerekítés round - function)
print(round(2.666666666, 2)) # /vessző után hány tizedesig kerekítsen
print(8 // 3) #/dupla perjel mindig int osztályt ad 

result = 4 / 2 #/változóban integer lesz
result /= 2
print(result)

score = 1
#Users scores a point.
score += 1
print(score)

score = 0
height = 1.8
isWinning = True
#f-String
print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")