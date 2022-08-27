total = 0
for number in range(1, 101):
    if number % 2 == 0:             # Csak a páros számokat adja össze 1-100-ig
        total += number
print(total)

total1 = 0
for number in range(1, 101):
    total1 += number                # Minden számot összead 1-100-if
print(total1)