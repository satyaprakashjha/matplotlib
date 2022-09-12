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