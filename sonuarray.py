# #Array using for loop with index
# import array
# stu_roll = array.array('i', [101,102,103,104,105])
# n = len(stu_roll)
# for i in range(n):
#     print(stu_roll[i])

# # Array using while loop with index
# import array
# stu_roll = array.array('i', [10,20,30,40,50,60])
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1

# #append method is to add an 
# #element at the end of the exixting 
# # array using  while loop

# import array
# stu_roll = array.array('i', [10,20,30,40,50])
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1
# print("array after append")
# stu_roll.append(60)
# stu_roll.append(70)
# stu_roll.append(80)
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1

# #append method getting input from user by 
# # array using for loop

# import array
# stu_roll = array.array('i',[])
# n = int(input("Enter number of elements: "))

# for i in range(n):
#    stu_roll.append(int(input("enter elements: ")))

# for i in range(len(stu_roll)):
#     print(stu_roll[i])


# #append method getting input from user by 
# # array using while loop

# import array
# stu_roll = array.array('i',[])
# n = int(input("Enter no. of elements: "))

# i = 0
# while i<n:
#     stu_roll.append(int(input("Enter elements: ")))
#     i+=1

# j = 0
# while (j<len(stu_roll)):
#     print(stu_roll[j])
#     j+=1

# from array import *
# stu_roll = array('i',[])
# n = int(input("Enter no. of elements: "))

# for i in range(n):
#     stu_roll.append(int(input("Enter elements:")))

# for i in range(len(stu_roll)):
#     print(stu_roll[i])

# print()


# from array import *
# stu_roll = array('i', [])
# n = int(input("Enter no. of elements: "))

# i = 0
# while i<n:
#     stu_roll.append(int(input("Enter elements:")))
#     i+=1

# j = 0
# while j<(len(stu_roll)):
#     print(stu_roll[j])
#     j+=1

# insert method use to insert element 
# at particular location

# import array
# stu_roll = array.array('i', [10,20,30,40,50])
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1
# print("array after insert")
# stu_roll.insert(1,15)
# stu_roll.insert(3,25)
# stu_roll.insert(5,35)
# stu_roll.insert(7,45)
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1

#pop method use to remove the last element
# of exixting array


import array
stu_roll = array.array('i', [10,20,30,40,50])
n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1
print("array after pop")
stu_roll.pop()

n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1

#pop(n) method use to remove the element
# by position of exixting array and also can return the value

import array
stu_roll = array.array('i', [10,20,30,40,50])
n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1
print("array after pop(n)")
r = stu_roll.pop(1)

n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1
print("removed element:", r)

print()

from array import *
stu_roll = array('i', [101,102,103,104,105])
_New = array('i', [107,108,109])
n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1

print("Array After extend")
stu_roll.extend(_New)
n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1


