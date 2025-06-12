car = {
    "company" : "honda",
    "model" : "civic",
    "year" : 2004   
}
print(car)
print(car['model'])
print(len(car))
print(type(car))

car1 = dict(brand = "Mercedez", model = "S Class", year = 2022)
print(car1)
x = car1.get("model")
print(x)
x1 = car1.keys()
print(x1)
car1["color"] = "white"
print(car1)
x2 = car1.values()
print(x2)
car1 ["year"] = 2023
print(car1)
z = car1.items()
print(z)

car2 = {
    "model" : "G-Wagon",
    "brand" : "Mercedez",
    "year" : 2022,
    "condition" : "good"
}
car2["year"] = 20225
print(car2)
y1 = car2.pop("year")
print(y1)
y2 = car2.popitem()
print(y2)
del car2["model"]
print(car2)
for a1 in car2:
    print(a1)

car3 = dict(model = "G-wagon", company = "Mercedez", year = 2022, Price = 12.2)
for a2 in car3:
    print(car3[a2])
    print(a2)

car4 = dict(model = "G-wagon", company = "Mercedez", year = 2022, Price = 12.2)
for x9 in car4.values() :
    print(x9)
for x10 in car4.keys() :
    print(x10)
for x11, x12 in car4.items() :
    print(x11, x12)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
print(myfamily["child2"]["name"])
for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])

aa = 200
bb = 300
if aa > bb :
   print('true')
else :
   print('flase')

aa1 = 100
bb1 = 200
cc1 = 300
print("true") if aa1 > bb1 else  print('false') if bb1 > cc1 else print('true')

i = 1
while i < 6 :
   print(i)
   i += 1

fruits = ["apple", "mango", "banana"]
for x in fruits :
   print(x)

for x in "banana" :
   print(x)

vegetables = ["potato", "tomato", "brinjal", "radish", "onion"]
for x in vegetables :
   print(x)
   if x == "radish" :
        break

phonebook = {}
phonebook['Raj'] = 9876543210
phonebook['Rajesh'] = 9876543211
print(phonebook)
del phonebook['Raj']
print(phonebook)

phonebook2 = {
   "Raj" : 9876543210,
   "Rajesh" : 9876543211,
}
print(phonebook2)

# Iterating over dictonaries 
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

phonebook3 = {
   "Raj" : 9876543210,
   "Rajesh" : 9876543211,
   "Rajeshwari" : 9876543212,
   "Maheshwari" : 9876543213,
}
phonebook3.pop("Maheshwari")
print(phonebook3)
