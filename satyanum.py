
import numpy as np
arr = np.array((1,2,3,4,5))
print(arr[1]+arr[3])

print(type(arr))

print(np.__version__)

import numpy as np
arr1 = np.array([[[1,2,3],[4,5,6]], [[1,2,3],[4,5,6]]])

print(arr1[0])


import numpy as np
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2[0,1])  

print(arr2[1,4])


import numpy as np
arr1 = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])

print(arr1[0,1,2])

# Numpy Array Slicing

import numpy as np
a = np.array([10,20,30,40,50,60,70])
print(a)
print(a[1:5])
print(a[4:])
print(a[:4])
print(a[-3:-1])
print(a[::2])

#Numpy 2-D Array Slicing

import numpy as np
b = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b)
print(b[1,1:4])
print(b[0:2, 1:2])
print(b[0:2, 1:4])

#Data type

import numpy as np

arr = np.array(['apple', 'banana', 'cherry', 'pineapple'], dtype='S')

print(arr.dtype)


# Converting Data type on existing arrays

import numpy as np
arr = np.array([1.1,2.1,3.1])
new_arr = arr.astype('i')

print(new_arr)
print(new_arr.dtype)

# float to integer

import numpy as np
arr = np.array([1.1,2.1,3.1])
new_arr = arr.astype(int)

print(new_arr)
print(new_arr.dtype)

# from integer to boolean

import numpy as np
arr = np.array([11,0,33])
new_arr = arr.astype(bool)

print(new_arr)
print(new_arr.dtype)

# Numpy array Copy VS view

import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)


import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

import numpy as np
arr = np.array([1,2,3,4,5])
x = arr.view()
y = arr.copy()

print(y.base)
print(x.base)   

# shape of an Array

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])

print(arr.shape)

# ndimn

import numpy as np
arr = np.array([1,2,3,4], ndmin= 5 )
print(arr)
print(arr.shape)

#Reshape

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2)
print(newarr)

# Flattening the Arrays

import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
newarr = arr.reshape(-1)
print(newarr)

#Arrays Iterating
# 1 D array
import numpy as np
arr = np.array([1,2,3])

for x in arr:
    print(x)

# 2 D array
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:
    print(x)

# Array Using nditer()
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for x in np.nditer(arr):
    print(x)

#Enumerated Iteration Using ndenumerate()
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

#Joining Arrays

#joining two arrays
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1, arr2))
print(arr)














