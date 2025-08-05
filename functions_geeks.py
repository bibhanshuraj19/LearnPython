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

