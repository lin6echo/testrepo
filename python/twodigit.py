from unittest import result


two_digit_number = input("Type a two digit number")

print(type(two_digit_number))

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

print(first_digit)
print(second_digit)

#result = first_digit + second_digit /45
#print(result)

result = int(first_digit) + int(second_digit) #/9
print(result)