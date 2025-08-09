class Dog :
    species = "canine"  # species is a class variable

    def __init__(self, name, age) : # here name and age are instance variable
        self.name = name
        self.age = age

# creating an object of the dog class
dog1 = Dog("John", 20)
print(dog1.species)
print(dog1.age)
print(dog1.name)

print(dog1.name, dog1.age, dog1.species)

# modify
Dog.species = "german"
print(dog1.species) # updated class variable

# Single Inheritance
class Cat :
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print(f"cat name is {self.name}")

class persian(Cat) :
    def sound(self):
        print("persian meow")

# Multilevel Inheritance
class GuideCat(persian):
    def guide(self):
        print(f"{self.name} guide cat!")

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("friendly")

class Golden(Cat, Friendly):
    def greet(self):
        print("Golden")

lab = persian("Buddy")
lab.display_name()
lab.sound()

guide_cat = GuideCat("Green")
guide_cat.display_name()
guide_cat.guide()

# Parent Class
class Dog :
    def sound(self):
        print("dog sound") # Default implementation

class Labrador(Dog) :
    def sound(self):
        print("labrador woof")

class Beagle(Dog):
    def sound(self):
        print("beagle woof")

class Calculator:
    def add(self, a, b=0, c=0):
        return a+b+c

dogs = [Dog(), Labrador(), Beagle()]
for dog in dogs :
    dog.sound()

calc = Calculator()
print(calc.add(1,2))
print(calc.add(1,2, 3))