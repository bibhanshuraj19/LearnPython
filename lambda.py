s1 = 'bibhanshu raj'
s2 = lambda func: func.upper()

print(s2(s1))
print("----------------------------------------")

x = lambda y : "Positive" if y > 0 else "Negative" if y < 0 else "Zero"
print(x(10))
print(x(-2))
print(x(0))
print("----------------------------------------")

square = lambda x : x ** 2
print(square(10))

def sqdef(x) :
    return x ** 2
print(sqdef(10))
print("----------------------------------------")

li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())
print("----------------------------------------")

check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(2))
print(check(3))
print("----------------------------------------")

calc = lambda x, y: (x+y,x*y)
res = calc(3,4)
print(res)
print("----------------------------------------")

diff = lambda x,y : (x-y)
res = diff(2,3)
print(res)
print("----------------------------------------")

n = [1,2,3,4,5,6,7,8,9]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))
print("----------------------------------------")

n = [1,2,3,4,5,6,7,8,9]
square = map(lambda x: x ** 2, n)
print(list(square))
print("----------------------------------------")

from functools import reduce
n = [1,2,3,4,5,6,7,8,9]
res = reduce(lambda x,y : x+y, n)
print(res)
