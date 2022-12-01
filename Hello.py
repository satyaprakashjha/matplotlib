# Day = input("Enter the day name ")
# if (Day == "monday"):
#     print("Today is working day")
# elif (Day == "tuesday"):
#     print("Also working day")
# elif (Day == "wednesday"):
#     print("Also working day")
# elif (Day == "thursday"):
#     print("Also working day")
# else:
#     print("Out of order")

#While loop
# a = 2
# while a<=20:
#     print(a)
#     a+=1

#While Else loop
# a = 11
# while a<=10:
#     print(a)
#     a+=1
# else:
#     print("when While condition is false so rest part executed")
# print("Rest of the code")

# i = 0
# while True:
#     i+=1
#     print(i)
#     if(i == 3):
#         break
# print("Rest code")

#Nested while loop

# i = 1
# while i<=3:
#     print("outer loop" , i)
#     i+=1
#     j = 1
#     while j<=5:
#         print("inner loop" , j)
#         j+=1
    
# print("Rest code")

#Range

# a = range(5,0,-1)
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print("welcome to the \"mumbaI\"")

# if 5<2 and 5<3:
#     print("if statement with logical operator")
#     print("statement 2")
# else:
#     print("Condition not true")
# print("rest code")

# a = int(input("Enter no. greater than 5" ))
# if a>5:
#     print("this is correct value", a)
# else:
#     print("you put the wrong value")
# print("End of the line")

# a = 5
# while a<=50:
#     print(a)
#     a+=5
# print("Rest of the code")

# import array
# stu_roll = array.array('i', [101,102,103,104,105])
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[2])
# print(stu_roll[3])
# print(stu_roll[4])

# from array import *
# stu_roll = array('f', [10.1,10.2,10.3,10.4,105.5])
# print(stu_roll[0])
# print(stu_roll[1])
# print(stu_roll[2])
# print(stu_roll[3])
# print(stu_roll[4])

# from array import *
# stu_roll = array('f', [10.1,10.2,10.3,10.4,105.5])
# n = len(stu_roll)
# for m in range(n):
#     print(m, "=", stu_roll[m])

# import array
# stu_roll = array.array('i', [101,102,103,104,105])
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1

# from array import *
# stu_roll = array('i', [101,102,103,104,105])
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1
# print("array after append")
# stu_roll.append(106)
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1

# from array import *
# stu_roll = array('i', [])
# n = int(input("Enter no of elements:"))
# for i in range(n):
#     stu_roll.append(int(input("Enter element:")))

# for i in range(len(stu_roll)):
#     print(stu_roll[i])


# from array import *
# stu_roll = array('i', [])
# n = int(input("Enter no. of elements:"))
# i = 0
# j = 0
# while i<n:
#     stu_roll.append(int(input("Enter elements:")))
#     i+=1
# while j<len(stu_roll):
#     print(stu_roll[j])
#     j+=1

#Insert

# from array import *
# stu_roll = array('i', [101,102,103,104,105])
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1

# print("Array after insert")
# stu_roll.insert(1,106)
# stu_roll.insert(3,107)
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1


#pop #Remove last elemnet

# from array import *
# stu_roll = array('i', [101,102,103,104,105])
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1

# print("Array After POP")
# stu_roll.pop()
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1

#pop # remove element with position no. and we can show that by print

# from array import *
# stu_roll = array('i', [101,102,103,104,105])
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1

# print("Array After POP")
# r = stu_roll.pop(3)
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1
# print("Removed element:", r)




#Remove (element)

# from array import *
# stu_roll = array('i', [101,102,103,104,105])
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1

# print("Array After remove")
# r = stu_roll.remove(103)
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1
# print("Removed element:", r)

# index (position no.)

# from array import *
# stu_roll = array('i', [101,102,101,104,105])
# print(stu_roll.index(104))


# reverse()

# from array import *
# stu_roll = array('i', [101,102,103,104,105])
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1

# print("Array After reverse")
# r = stu_roll.reverse()
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1
# print("Reverse element:", r)

#extend()

# from array import *
# stu_roll = array('i', [101,102,103,104,105])
# _New = array('i', [107,108,109])
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1

# print("Array After extend")
# stu_roll.extend(_New)
# n = len(stu_roll)
# i = 0
# while i<n:
#     print(stu_roll[i])
#     i+=1


# #slicing

# from array import *
# stu_roll = array('i', [101,102,103,104,105,106,107])
# print("original array")
# n = len(stu_roll)
# for i in range(n):
#     print(i, "=", stu_roll[i])

# print("After slicing")
# s = stu_roll[0:7:4]
# for i in s:
#     print(i)

















     



 



