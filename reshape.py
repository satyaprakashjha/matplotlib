# reshape(array_name,(n,r,c)) 
# n = no. of array in the resultant array
# r = no.of rows
# c = no. of columns
from numpy import *
a = array([1,2,3,4,5,6,7,8,9,10,11,12])
r = reshape(a, (2,3,2))
print(r)


from numpy import *

a = array([[10,20,30], [40,50,60]])
b = reshape(a, 6)
print(b)

# flatten() method
from numpy import *
e = array([[11,12,13], [14,15,16]])
f = e.flatten()
print(e)
print(f)

