height = input("enter your height in m:")
weight = input("enter your weight in kg:")

bmi = int(weight) / float(height) ** 2
#print(type(height)) /class 'str'
#print(bmi)
bmi_as_int = int(bmi) #/The int() function converts the specified value into an integer number.
print(bmi_as_int)