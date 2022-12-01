# # import numpy
# # stu_roll = numpy.array([101,102,103,104,105])
# # print(stu_roll)
# # print(stu_roll.dtype)
# # print(stu_roll[0])
# # print(stu_roll[1])
# # print(stu_roll[2])
# # print(stu_roll[3])
# # print(stu_roll[4])


# # from numpy import *
# # stu_roll = array([101,102,103,104,105])
# # print(stu_roll)
# # print(stu_roll.dtype)

# # stu_roll[1] = 120

# # print(stu_roll[0])
# # print(stu_roll[1])
# # print(stu_roll[2])
# # print(stu_roll[3])
# # print(stu_roll[4])

# #array using for loop in Numpy

# # from numpy import *
# # stu_roll  = array([101,102,103,104,105])

# # stu_roll[1] = 120

# # n = len(stu_roll)

# # for i in range(n):
# #     print(i, '=', stu_roll[i])


# #array using while loop in Numpy

# # from numpy import *
# # stu_roll  = array([101,102,103,104,105])

# # n = len(stu_roll)

# # i = 0
# # while i<n:
# #     print("index", i, '=', stu_roll[i])
# #     i+=1


# #linspace in numpy using while loop
# it is use to creat an array with 
# evenly spaced number ( default 50 divide)


# # from numpy import *
# # stu_roll  = linspace(1,20)

# # n = len(stu_roll)

# # i = 0
# # while i<n:
# #     print("index", i, '=', stu_roll[i])
# #     i+=1


# #linspace in numpy using for loop

# # from numpy import *
# # stu_roll  = linspace(1,8,5)

# # n = len(stu_roll)

# # for i in range(n):
# #     print(i,"=", stu_roll[i])


# # logspace in numpy using for loop
#start with base** end with base **
# default base 10

# # from numpy import *
# # stu_roll = logspace(1,3,5, base=12)

# # n = len(stu_roll)

# # for i in range(n):
# #     print(i, "=", stu_roll[i])


# # logspace in numpy using while loop

# # from numpy import *
# # stu_roll = logspace(1,3,5, base=12)

# # n = len(stu_roll)
# # i = 0
# # while i<n:
# #     print(i, "=", stu_roll[i])
# #     i+=1



# # arange in numpy
# # from numpy import *
# # a = arange(1,10,2)
# # print(a)

# # zeros in numpy
# # from numpy import *
# # a = zeros(5, dtype=int)
# # print(a)

# # ones in numpy
# # from numpy import *
# # a = ones(5)
# # print(a)


# #math function

# from numpy import *
# a = array([101,102,103,104,105])
# b = array([1,2,3,4,5])
# c = a + b
# n = len(c)

# for i in range(n):
#     print(i, "=", c[i])

# # compare array

# from numpy import *
# a = array([100,200,300,400,500])
# b = array([100,20,30,400,50])
# c = a > b
# print(c)

# #any and all function

# from numpy import *
# a = array([100,200,300,400,500])
# b = array([100,200,300,400,500])
# c = a == b
# print(all(c))


# #where function

# from numpy import *
# a = array([100,120,300,40,500])
# b = array([10,250,30,400,50])
# c = where(a>b, a, b)
# print(c)

# #nonzero function

# from numpy import *
# a = array([100,0 ,250,30,0,50,145,0])
# n = nonzero(a)
# print(n)

# #view function
# from numpy import *
# a = array([100,200,250,30,0,50,145,0])
# b = a.view()
# a[1] = 80
# print(a)
# print(b)
# print(id(a), "a")
# print(id(b), "b")

# #copy method
# from numpy import *
# a = array([100,200,250,30,0,50,145,0])
# b = copy(a)
# a[1] = 500
# print(a)
# print(b)
# print(id(a), "a")
# print(id(b), "b")


# from numpy import *
# n = int(input("Enter number: "))
# a = zeros(n, dtype=int)
# for i in range(len(a)):
#     x = int(input("Enter elemnet: "))  
#     a[i] = x     

# for i in range(len(a)):
#     print(a[i])



# from numpy import *
# a = array([101,102,103,104,105])
# b = array([1,2,3,4,5])
# c = a - b
# n = len(c)

# for i in range(n):
#     print(i, "=", c[i])


# from numpy import *
# a = array([100,200,300,400,500])
# b = array([100,20,30,400,50])
# c = a > b
# print(c)



from numpy  import *


n = int(input("Enter no. of elements: "))
a = zeros(n)

u = len(a)

i = 0
j = 0

while i<u:
    x = int(input("Enter elements:"))
    a[i] = x
    i+=1
while j<u:
    print(a[j])
    j+=1




