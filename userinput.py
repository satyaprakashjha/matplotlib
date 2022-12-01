# for loop
# from numpy import *
# m = int(input("Enter no. of rows: "))
# n = int(input("Enter no. of column: "))
# a = zeros((m,n), dtype=int)

# u = len(a)

# print(a)

# for i in range(u):
#     for j in range(len(a[i])):
#         x = int(input("Enter elements: "))
#         a[i][j] = x

# for i in range(u):
#     for j in range(len(a[i])):
#         print(a[i][j])
# print(a)

# while loop

from numpy import *

m = int(input("Enter no. of rows: "))
n = int(input("Enter no. of column: "))
a = zeros((m,n), dtype= int)
print(a)

u = len(a)
print(u)

i = 0

while i < u:
    j = 0
    while j < len(a[i]):
        x = int(input("Enter elements: "))
        a[i][j] = x
        j+=1
    i+=1

print(a)

i = 0
while i < u:
    j = 0
    while j < len(a[i]):
        print(a[i][j])
        j+=1
    i+=1

print(a)

