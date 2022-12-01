# from numpy import *

# a = array([[10,20,30,40],
#            [50,60,70,80]])

# n = len(a)
# for i in range(n):
#     for j in range(len(a[i])):
#         print(a[i][j])
#     print()

from numpy import *

x = array([[11,12,13,14],
             [15,16,17,18]])

n = len(x)

i = 0
while i < n:
    j = 0
    while j < len(x[i]):
        print(x[i][j])
        j+=1
    i+=1
    print()





