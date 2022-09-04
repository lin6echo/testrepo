def myfunc(param1 = 'default'):
    print('My first python function!')
    print('My first python function! {}'.format(param1))
    
myfunc()
# ------------------------------------------------------------------
def hello():
    print('hello')
    
hello()
# ------------------------------------------------------------------
def hello():
    return ('hello')
    
result = hello()
print(result)