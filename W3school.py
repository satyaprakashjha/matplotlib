


# print("Hello, World!")
# #BMI calculator

# name1 = 'YK'
# height1 = 2
# weight1 = 90

# name2 = "YK's Sister"
# height2 = 1.8
# weight2 = 70

# name3 = "YK's Brother"
# height3 = 2.5
# weight3 = 160

# def bmi_cal(name, height, weight):
#     bmi = weight / (height**2)
#     print("bmi")
#     print(bmi)
#     if bmi < 25:
#         return name + " is not overweight"
#     else:
#         return name + " is overweight "  

# result1 = bmi_cal(name1, height1, weight1)
# result2 = bmi_cal(name2, height2, weight2)
# result3 = bmi_cal(name3, height3, weight3)

# print(result1)
# print(result2)
# print(result3)



# x = "awesome"
# def add():
#     global x
#     x = "fantastic"
    

# add()
# print("python is " + x)

# thislist = ["apple", "mango", "orange"]
# thislist.append("banana")
# print(thislist)

# mylist = ["apple", "mango", "orange"]
# mylist.insert(0, "potato")
# print(mylist)

# firstlist = ["apple", "mango", "orange"]
# secondlist = ["potato", "tomato", "onion"]
# firstlist.extend(secondlist)
# print(firstlist)

# list1 = ["india", "brazil", "america"]
# tuple1 = ("kiwi", "apple")
# list1.extend(tuple1)
# print(list1)

# fruits = ["banana", "cheery", "papaya"]
# fruits.remove("papaya")
# print(fruits)


# fruit = ["banana", "cheery", "papaya"]
# fruit.pop()
# print(fruit)

# fruit = ["banana", "cheery", "papaya"]
# fruit.pop(1)
# print(fruit)


# thislist1 = [10, 20, 30, 40, 50]
# del thislist1[1]
# print(thislist1)

# thislist = [10, 20, 30, 40, 50]
# del thislist
# print(thislist)

# listclear = [10, 20, 25, 40, 50]
# listclear.clear()
# print(listclear)


from ast import If


listx = ["one", "two", "three"]
for x in range(len(listx)):
    print(x, listx[x])

listz = [10, 20,30,40,50]
i = 0
while i < len(listz):
    print(listz[i])
    i+=1

lists = ["one", "two", "three"]
for x in lists:
     if x == "two":
        break
     print(x)
   
listm = [10,20,30,40]
for i in listm:
    if i == 30:
        continue
    print(i)

fruit1 = ["apple", "kiwi", "orange", "banana", "cheery"]
fruit2 = []

for i in fruit1:
    if "a" not in i:
        fruit2.append(i)

print(fruit2)

fruit5 = ["apple", "kiwi", "orange", "banana", "cheery"]
fruit5.sort()
print(fruit5)

fruit9 = [10,20,30,40,50,60,70,80]
fruit9.sort(reverse=True)
print(fruit9)