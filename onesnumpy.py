# creating 2d array using ones() function

from numpy import *
a = ones((3,2), dtype= int)
print(a)
n = len(a)

for i in range(n):
    for j in range(len(a[i])):
        print(a[i][j])
    print()