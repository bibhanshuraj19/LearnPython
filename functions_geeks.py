def greet() :
    print("hello")

greet()

def evenODD(x : int) :
    if (x % 2 == 0) :
        return "even"
    else :
        return "odd"

print(evenODD(3))
print(evenODD(8))
print("----------------------------------------")

def myFun(x, y=50) :
    print("x :",x)
    print("y :",y)
myFun(10)
print("----------------------------------------")

def name(fname,lname) :
    print(fname,lname)
name("bibhanshu","raj")
print("----------------------------------------")

def nameAge(name,age) :
    print("Hi I am : ",name)
    print("I am : " ,age)
nameAge("raj",19)
print("----------------------------------------")

def myFunc(*argv) :
    for arg in argv :
        print(arg)
myFunc('hello','welcome','to','nowhere')
print("----------------------------------------")

def myFun(**kwargs) :
    for key, value in kwargs.items() :
        print("%s == %s" % (key,value))
myFun(first='Geeks', mid='for', last='Geeks')
print("----------------------------------------")

def evenODD(x) :
    """function to change if the number is even or odd"""

    if x % 2 == 0 :
        return "even"
    else :
        return "odd"

print(evenODD.__doc__)    # the __doc__ is used to print the docstring of a function
print("----------------------------------------")

def f1() :
    s = 'I love Python'

    def f2() :
        print(s)

    f2()
f1()
print("----------------------------------------")

def cube(x) :
    return x * x * x
cube_l = lambda x : x * x * x
print(cube(7))
print(cube_l(7))
print("-----------------------------------------")

def square_value(num) :
    """this function return the square value of num"""
    return num**2
print(square_value(3))
print(square_value(-3))
print(square_value.__doc__)
print("----------------------------------------")

def myFun(x) :
    x[0] = 20

lst = [10,11,12,13,14,15]
myFun(lst)
print(lst)
print("----------------------------------------")

def myFun(x) :
    x = [20,30,40]
lst = [10,11,12,13,14,15]
myFun(lst)
print(lst)
print("----------------------------------------")

def myFun(x) :
    x = 20

x = 10
myFun(x)
print(x)
print("----------------------------------------")

def factorial(n) :
    if n == 0 :
        return 1
    else :
        return n * factorial(n - 1)
print(factorial(5))
print("----------------------------------------")

