previous = int(input("What was the previous number?"))
#print(previous)
previous_number = previous

actual = int(input("What is the new number?"))
#print(actual)
actual_number = actual

result = actual_number - previous_number
print(result)

supported = 210
basic = supported * 37.6
more = (result - supported) * 70.1

def myfunc():
    if result <= supported:
        print(result * 37.6)
    else:
        print(basic + more)
        
myfunc()

    



