my_stuff = {'key1': 123, 'key2': 'value2', 'key3': {'keyalt': [1, 2, 'grabMe']}}
print(my_stuff['key3']['keyalt'][2])                           # return: grabMe

my_stuff = {'lunch': 'pizza', 'breakfast': 'eggs'}
print(my_stuff['lunch'])                                    # return: pizza

my_stuff['lunch'] = 'burger'
print(my_stuff['lunch'])                                    # return: burger

my_stuff['dinner'] = 'pasta'
print(my_stuff)                                             # return: {'lunch': 'burger', 'breakfast': 'eggs', 'dinner': 'pasta'}

# 06/04:39