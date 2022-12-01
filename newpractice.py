# create array example

# from array import *
# stu_roll = array('i', [10,20,30,40,50])
# n = len(stu_roll)
# for i in range(n):
#     print(i, stu_roll[i])

# while loop array

# from array import *
# stu1 = array('i', [101,102,103,104,105])
# n = len(stu1)
# i = 0
# while i<n:
#     print(stu1[i])
#     i+=1

# # append()

# from array import *
# stu_roll = array('i', [101,102,103,104,105])
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i+=1

# print("array after append")
# stu_roll.append(106)
# stu_roll.append(107)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i+=1

# # getting user input by for loop
# from array import *
# stu_roll = array('i', [])
# n = int(input("Enter no. of elements:"))

# for i in range(n):
#     stu_roll.append(int(input("enter element:")))

# for i in range(len(stu_roll)):
#     print(stu_roll[i])

# getting user input by while loop

# from array import *
# stu_roll = array('i', [])
# n = int(input("enter no. of elements:"))

# i = 0

# while i < n:
#     stu_roll.append(int(input("enter the element:")))
#     i+=1

# j = 0

# while (j < len(stu_roll)):
#     print(stu_roll[j])
#     j+=1

# insert method

# from array import *

# stu_roll = array('i',[101,102,103,104,105])
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i+=1
# print("Array after insert")
# stu_roll.insert(1,106)
# stu_roll.insert(3,107)
# n = len(stu_roll)
# i = 0
# while i < n:
#     print(stu_roll[i])
#     i+=1

# array reverse method

from array import *
stu = array('i', [101,102,103,104,105])
n = len(stu)
i = 0
while i < n:
    print(stu[i])
    i+=1
print("Array after reverse")
stu.reverse()
n = len(stu)
i = 0
while i < n:
    print(stu[i])
    i+=1

# array extend method

# from array import *
# stu = array('i', [101,102,103,104,105])
# arr = array('i', [106,107,108])
# n = len(stu)
# i = 0
# while i < n:
#     print(stu[i])
#     i+=1
# print("Array after extend")
# stu.extend(arr)
# n = len(stu)
# i = 0
# while i < n:
#     print(stu[i])
#     i+=1

# slicing on array

from array import *
stu = array('i', [101,102,103,104,105,106,107])
print("original array")
n = len(stu)
for i in range(n):
    print(i, "=",  stu[i])

print("after slicing")

a = stu[:5]
for i in a:
    print(i)






  
    







