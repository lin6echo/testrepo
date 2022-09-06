x = 50

def func(x):
    print('x is: ', x)
    x = 1000
    print('local x is changed to: ', x)
    
func(x)
print(x)
#--------------------------------------------------
def func1():
    print('x is: ', x)
    
func1()
#---------------------------------------------------
def func2():
    x = 100
    print(x)
    
func2()