mylist = [1, 2, 3, ['a', 'b', 'c']]
print(mylist[3])                                # return: ['a', 'b', 'c']
print(mylist[3][1])                             # return: b

matrix = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]

first_col = [row[0] for row in matrix]

print(first_col)