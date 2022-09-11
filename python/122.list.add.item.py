mylist = ['a', 'b', 'c', 'd', 'e']
print('Before reassignment:')
print(mylist)
mylist[0] = 'New item'
print('After reassignment:')
print(mylist)                                   # return: ['New item', 'b', 'c', 'd', 'e']

mylist = ['a', 'b', 'c', 'd', 'e']
mylist.append("New item")
print(mylist)                                   # return: ['a', 'b', 'c', 'd', 'e', 'New item']

mylist = ['a', 'b', 'c', 'd', 'e']
mylist.append(['x', 'y', 'z'])
print(mylist)                                   # return: ['a', 'b', 'c', 'd', 'e', ['x', 'y', 'z']]

mylist = ['a', 'b', 'c', 'd', 'e']
listtwo = ['x', 'y', 'z']
mylist.extend(listtwo)
print(mylist)                                   # return: ['a', 'b', 'c', 'd', 'e', 'x', 'y', 'z']
