# import numpy
# r = int(input("Enter no. of rows: "))
# n = int(input("Enter no. of column: "))


# a = numpy.zeros((r,n), dtype=int)
# u = len(a)

# for i in range(u):
#     for j in range(len(a[i])):
#         x = int(input("Enter element:"))
#         a[i][j] = x

# for i in range(u):
#     for j in range(len(a[i])):
#         print(i,j, "=", a[i][j])
# print(a[0,:])


# name = "geekyshows is The best youtuber"

# print(name)
# print(name.upper())
# print(name.lower())
# print(name.swapcase())
# print(name.title())


# from numpy import *
# a = array([[1,2,3],
#            [4,5,6],
#            [7,8,9]])

# print("original array")
# print(a)

# print(a[1:3,1:3])

# import numpy as np
# a = np.array([1,2,3])
# b = np.array([2,3,4])
# c = np.column_stack((a,b))
# print(c)

#BMI Calculater

name1 = "sonu"
height_m1 = 2
weight_kg1 = 90

name2 = "Ram"
height_m2 = 1.8
weight_kg2 = 70

name3 = "Mohan"
height_m3 = 2.5
weight_kg3 = 160

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg/(height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi <25:
        return name + " is not overweight "
    else:
        return name + " is overweight"

result1 = bmi_calculator(name1,height_m1,weight_kg1)
result2 = bmi_calculator(name2,height_m2,weight_kg2)
result3 = bmi_calculator(name3,height_m3,weight_kg3)

print(result1)
print(result2)
print(result3)

# def my_function1():
#     print("Hello from a function")
# print("This is outside the function")
# my_function1()



# def function2(x):
#     return 2 * x

# a = function2(3)
# print(a)

# b = function2(4)
# print(b)

# c = function2(5)
# print(c)




# def function3(x,y):
#     return x+y

# a = function3(5,10)
# print(a)

# def function4(x):
#     print(x)
#     print("still in this function")
#     return 3*x
# f = function4(4)
# print(f)

# def function5(some_argument):
#     print(some_argument)
#     print("Also in this function")
# function5(4)







# import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# if x:
#     print("yes")

# price = 49
# txt = "The price is {} dollars"
# print(txt.format(price))


# quantity = 3
# itemno = 576
# price = 49

# txt1 = "I want {} pieces of item no {} for {:.2f} dollars."
# print(txt1.format(quantity, itemno,price))

