import random

mylist = list("ABCDEFGH")
a = random.choice(mylist)
print(a)

mylist = list("ABCDEFGH")
a = random.sample(mylist, 3)
print(a)

mylist = list("ABCDEFGH")
a = random.choices(mylist, k=3)
print(a)

random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1,10))






