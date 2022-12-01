# zeros numpy 2d array for loop with index

# from numpy import *
# a = zeros((3,2), dtype= int)

# n = len(a)

# for i in range(n):
#     for j in range(len(a[i])):
#         print(i , j, "=", a[i][j])
#     print()

# zeros numpy 2d array while loop with index

from numpy import*

a = zeros((3,2), dtype=int)

n = len(a)

i = 0
while i < n:
    j = 0
    while j < len(a[i]):
        print(i , j, "=" , a[i][j])
        j+=1
    i+=1
    print()
