
# defining funtion for addition
def add():
    x = 10
    y = 20
    c = x + y
    print(c)

add()

# defining function with parameter

def add(y):
    x = 10
    c = x + y
    print(c)

add(50)

# keyword arguments

def show (name, age):
    print(name, age)

show(name = "geekyshows", age = 62)