x = [1, 2, 3, 4, 5]

out = [num**2 for num in x]
print(out)

out = []

for num in x:
    out.append(num**2)
    
print(out)