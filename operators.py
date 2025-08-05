number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

helloworld = "hello" + " " + "world"
print(helloworld)

hellos = "hello\n" * 10
print(hellos)

even = [2,4,6,8]
odd = [1,3,5,7]
all = odd + even
print (all)

print([1,3,4,5]*3)

x = object()
y = object()

x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list


a = 13
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

a = True
b = False
print(a and b)
print(a or b)
print(not b)

a = 10
b = 4

print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)
print("------------------------------")

a = 10
b = a
print(b)
b += a
print(b)
print("------------------------------")


a = 10
b = 20
c = a
print(a is not b)
print(a is c)
print("------------------------------")


x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list) :
    print("x is not in list")
else :
    print("x is in list")

if (y in list) :
    print("y is in list")
else :
    print("y is not in list")
print("------------------------------")


a, b = 10, 20
min = a if a < b else b
print(min)
print("------------------------------")

expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else :
    print("Good Bye!")
print("------------------------------")

num1 = 5
num2 = 2

sum = num1 + num2
difference  = num1 - num2
product = num1 * num2
quotient = num1 / num2
remainder = num1 % num2

print("Sum : ",sum)
print("Difference : ",difference)
print("Product : ",product)
print("Quotient : ",quotient)
print("Remainder : ",remainder)
print("------------------------------")

num1 = 30
num2 = 35

if num1 > num2 :
    print("num1 > num2")
elif num1 < num2 :
    print("num1 < num2")
else :
    print("num1 = num2")