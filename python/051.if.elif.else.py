a = 33
b = 34
if b > a:
    print("b is greater than a")

c = 33
d = 33
if c > d:
    print("c is greater than d")
elif c == d:
    print("c and d are equal")

e = 200
f = 33
if f > e:
    print("f greater than e")
elif e == f:
    print("e and f are equal")
else:
    print("e greater than f")

# multiple else statements on the same line
j = 333
k = 333
print("A") if j > k else print("=") if j == k else print("B")