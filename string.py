str = """Hello guys
my name is
satyaprakash"""
print(str)

# upper case

a = "hello, world!"
b = a.upper()
print(a.upper())
print(b)

# lower case

a = "hello, world!"
l = a.lower()
print(a.lower())
print(l)

# remove whitespace

a = " hello, world! "
print(a)
b = a.strip()
print(a.strip())

# replace

a = "hello my name is sonu"
b = a.replace("sonu", "satyaprakash")
print(b)

# split

a = " hello world , this is india"
b = a.split(",")
print(b)

# concatination

a = "hello"
b = "world"
c = a + " " + b
print(c)

# format()method using placeholder {}

age = 36
txt = "my name is jhon, and my age is {}"
print(txt.format(age))


quantity = 3
itemno = 567
price = 25.75
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# using index number {0}

quantity = 3
itemno = 567
price = 25.75
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# capitalize() upper case the first letter
txt = "hello, and welcome to my world."
x = txt.capitalize()
print(txt)
print(x)