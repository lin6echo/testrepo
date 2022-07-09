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
