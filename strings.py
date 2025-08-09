name = "raj"
print("hello, %s" % name)
age = 20
place = "siwan"
print("%s is %d years old and lives in %s" % (name, age,place))

mylist = [1,2,3,]
print("A list : %s" %mylist)



data = ("John", "Doe", 53.44)
format_string = ("Hello %s %s. Your current balance is $%f" % (data))

print(format_string)


astring = "Hello world"
astring2 = "Hello world!"
print(astring,astring2)
print(len(astring))
print(astring.count("o"))
print(astring.index("o"))

print(astring[3:7:2])
print(astring[::-1])
print(astring.upper())

print(astring.startswith("Hello"))
print(astring.endswith("asassadasd"))

afterwards = astring.split(" ")

name = "bibhanshu Raj"
new = "B" + name[1:]
print(new)

