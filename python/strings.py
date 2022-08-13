my_string = "Hello World"
print(my_string)

my_string = 'I\'m a programmer' # backslash
print(my_string)

my_string = """Hello
World"""
print(my_string)

my_string = """Hello \
World"""
print(my_string)

my_string = "Hello World"
char = my_string[0]
print(char)

substring = my_string[1:5]
print(substring)
substring = my_string[::2]
print(substring)
substring = my_string[::-1]
print(substring)

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

greeting = "Hello"
for i in greeting:
    print(i)
    
if "e" in greeting:
    print("yes")
else:
    print("no")
    
my_string = "   Hello World     "
my_string = my_string.strip()
print(my_string)

my_string = "Hello World"
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith("H"))
print(my_string.endswith("d"))
print(my_string.find("o"))
print(my_string.count("o"))
print(my_string.replace("World", "Universe"))

my_string = "how are you doing"
my_list = my_string.split()
print(my_list)

my_string = "how,are,you,doing"
my_list = my_string.split(",")
print(my_list)
new_string = ' '.join(my_list)
print(new_string)
#..............................................
my_list = ["a" ]* 1000000


from timeit import default_timer as timer
# bad
start = timer()
my_string = ""
for i in my_list:
    my_string += i
stop = timer()
print(stop-start)


# good
start = timer()
my_string = "".join(my_list)
stop = timer()
print(stop-start)
#...............................................
var = "Tom"
my_string = "the variable is %s" % var # %s place holder for string
print(my_string)

var = 3
my_string = "the variable is %d" % var # %s place holder for integer
print(my_string)

var = 3.41411415666
my_string = "the variable is %f" % var 
print(my_string)

var = 3.41411415666
my_string = "the variable is %.2f" % var  # .2f ---- two digits -- return: 3.41
print(my_string)
#-------------------------------------------------------
var = 3.1541
my_string = "the variable is {}".format(var)
print(my_string)

var = 3.1541434
my_string = "the variable is {:.2f}".format(var)
print(my_string)

var = 3.1541434
var2 = 6
my_string = "the variable is {:.2f} and {}".format(var, var2)
print(my_string)

string1 = 123
string2 = 345
my_string = "Big numbers {} and {}".format(string1,string2)
print(my_string)

string1 = 123
string2 = 345
my_string = f"Big numbers {string1} and {string2}"
print(my_string)

string1 = 123
string2 = 345
my_string = f"Big numbers {string1*2} and {string2**2}"
print(my_string)




















