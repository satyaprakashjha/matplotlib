#zip() method

from audioop import add


x = [1,2,3,4]
y = [5,6,7,8]
z = []

for i, j in zip(x, y):
    z.append(i+j)
print(z)

# add()

import numpy as np
x = [1,2,3,4]
y = [5,6,7,8]
z = np.add(x,y)


print(z)

# create own function

import numpy as np
def myadd(x,y):
    return x+y
myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1,2,3,4],[5,6,7,8]))

#arithmetic function
#add()

import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.add(arr1,arr2)
print(newarr)

#subtraction
#subtract()

import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1,arr2)
print(newarr)

#multiplication
#multiply()

import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.multiply(arr1,arr2)
print(newarr)

#division
#divide()

import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.divide(arr1,arr2)
print(newarr)

#power
#power()

import numpy as np

arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([2, 2, 2, 2, 2, 2 ])

newarr = np.power(arr1,arr2)
print(newarr)

# Mod Power
a = int(input("Enter no."))
b = int(input("Enter no."))
m = int(input("Enter no."))
print(pow(a,b))
print(pow(a,b,m))