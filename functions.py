def myfunc(name) :
    print('fuck ' + name)
myfunc("email")

def id(fname,lname) :
    print("my name is " + fname + " " + lname)
id("bibhanshu" , "raj")

def data(*kids) :
    print ("my child name is " + kids[3])
data("kallu"," 2 years old", "he is black", "rishi") 

def data2(child1,child2) :
    print("my child is " + child1 + " and " + child2)
data2(child1 = "rahul" , child2 = "ayush")

def data3(**kid) :
    print("his last name is " + kid["lname"])
data3(fname = "bibhanshu" , lname = "raj")

def home(country = "india") :
    print("I am from " + country)
home()
home('norway')
home("sweden")
home("usa")

def eat(fruits) :
    for x in fruits :
        print (x)
fruit = ["apple","mango","kiwi"]
eat(fruit)

def mul(x1) :
    return 5 * x1
print(mul(5))
print(mul(3))

# ------x------x------x------x------x------x------x------x------xLAMBNDAx------x------x------x------x------x------x------x------x------x------x------x------x------x
x = lambda a : a + 2290
print(x(5))

y = lambda b : b * 50
print(y(5))

z = lambda c,d : c*d
print(z(10,20))

class Person :
    def __init__ (self,name,age) :
        self.name = name
        self.age = age
p1 = Person("john","26")
print(p1.name)
print(p1.age)

class School :
    def __init__(self,name,destination) :
        self.name = name
        self.place = destination
s1 = School("DPS","Delhi")
print(s1.name)
print(s1.place)