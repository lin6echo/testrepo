sum = 0
i = 1
n = 10

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)

i = 0
a = 'geeksforgeeks'
 
while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        break
         
    print('Current Letter :', a[i])
    i += 1