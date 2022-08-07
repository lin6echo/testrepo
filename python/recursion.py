# A számítástechnikában a verem (angolul stack) egy LIFO adatszerkezet, amelyben általában véges számú azonos típusú (méretű) adatot 
# lehet tárolni.

# Hagyományosan két alapműveletet értelmezünk rá:

# push (rárak): A verem tetejére helyez egy új adatot. Ha a verem betelt, akkor túlcsordulásos állapotba kerül.
# pop (levesz): A verem legfelső elemét leveszi és visszaadja. Ha a verem már üres, akkor alulcsordulásos állapotba kerül.
# A különböző megvalósításoknál előfordulhat, hogy a legfelső vagy tetszőleges elemet is el lehet érni annak levétele nélkül.

# A verem szokásos megvalósítása egy véges méretű összefüggő memóriaterület és egy veremmutató segítségével történik. 
# A memóriaterületet egyik vége felől töltjük föl, és a veremmutató mindig a legfölső elemre mutat 
# (a két művelet során ezt egyszerűen növelni vagy csökkenteni kell).

#Factorial
# Number! = Number x (Number - 1)
# def factorial(number):
#     return number * factorial(number - 1)
# print(factorial(5))
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)

# What is recursion?

# Recursion is the process of defining something in terms of itself.

# A physical world example would be to place two parallel mirrors facing each other. Any object in between them would be reflected recursively.

# Python Recursive Function
# In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

# The following image shows the working of a recursive function called recurse.

# Factorial of a number is the product of all the integers from 1 to that number. 
# For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720.

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 4
print("The factorial of", num, "is", factorial(num))




    
    