x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

value = (10, 20, 30, 40, 50)
my_tuple = list(value)
print(my_tuple)
print(type(my_tuple))
my_tuple = tuple(my_tuple)

mando = ["Mandalorian", "Grogu", "Ahsoka Tano", "Bo Katan", "Boba Fett"]
print(mando)
print(type(mando))

mando_tuple = tuple(mando)
print(mando_tuple)
print(type(mando_tuple))