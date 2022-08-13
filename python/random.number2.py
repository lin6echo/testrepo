import secrets

a = secrets.randbelow(10)
print(a)

a = secrets.randbits(4)
print(a)

mylist = list('ABCDEFGH')
a = secrets.choice(mylist)
print(a)