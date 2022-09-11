previous = int(input("What was the previous number?"))

actual = int(input("What is the new number?"))

result = actual - previous

print(result)

supported = 210
basic = supported * 37.6
more = (result - supported) * 70.2

def myfunc():
    if result <= supported:
        print(result * 37.6)
    else:
        print(basic + more)
        
myfunc()

    



