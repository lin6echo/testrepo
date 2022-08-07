# Errors and exceptions

# a = [5] print(a)              # return: SyntaxError: invalid syntax

# a = 5 + '10'                  # return: TypeError: unsupported operand type(s) .....   

# import somemodule             # return: ModuleNotFoundError: No module named 'somemodule'

# a = 5
# b = c                         # return: NameError: name 'c' is not defined

# f = open('somefile.txt')      # return: FileNotFoundError: [Errno 2] No such file or directory: 'somefile.txt'

# a = [1, 2, 3]
# a.remove(4)                   # return: ValueError: list.remove(x): x not in list

# a = [1, 2, 3]
# a[4]                          # return: IndexError: list index out of range

# my_dict = {'name':'Max'}
# my_dict['age']                # return: KeyError: 'age'

# x = -5
# if x < 0:
#     raise Exception('x should be positive')   # return: Exception: x should be positive

# x = -5
# assert (x >= 0)               # return: AssertionError

# x = -5
# assert (x >= 0), 'x is not positive'              # return: AssertionError: x is not positive

# a = 5 / 0                     # return: ZeroDivisionError: division by zero

try:
    a = 5 / 0
except:
    print('an error happened')  # return: an error happened
    
try:
    a = 5 / 0
except Exception as e:
    print(e)                    # return: division by zero
    
try:
    a = 5 / 1
    b = a + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up ...')
#.........................................................  
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too hight')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)
try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)  















