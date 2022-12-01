from array import *
stu_roll = array('i', [101,102,103,104,105])
n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1

print("Array After POP")
r = stu_roll.pop(3)
n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1
print("Removed element:", r)



from array import *
stu_roll = array('i', [101,102,103,104,105])
n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1

print("Array After remove")
r = stu_roll.remove(103)
n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1



from array import *
stu_roll = array('i', [101,102,101,104,105])
print(stu_roll.index(101))


from array import *
stu_roll = array('i', [101,102,103,104,105])
n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1

print("Array After reverse")
stu_roll.reverse()
n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1



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



from array import *
stu_roll = array('i', [101,102,103,104,105,106,107])
print("original array")
n = len(stu_roll)
for i in range(n):
    print(i, "=", stu_roll[i])

print("After slicing")
s = stu_roll[-4:]
for i in s:

    print(i)



from numpy import *
stu_roll = zeros(n, dtype=int)
n = int(input("Enter no of element: "))


i = 0
j = 0
while i<n:
    x = int(input("Enter element: "))
    stu_roll[i] = x
    i+=1

while j<len(stu_roll):
    print(stu_roll[j])
    j+=1
