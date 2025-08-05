s = 'Welcome to here'
print(s)

print(type(s))

print(s[0])
print(s[-1])

a = []
a = [1,2,3]
print(a)

b = ['raj',1,3,4]
print(b)

a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(a[0])
print(a[2])

print("Accessing element using negative indexing")
print(a[-1])
print(a[-2])

tup2 = ('geeks', 'for')
print(tup2)


tup1 = tuple([1,2,3,4,5,6])
print(tup1[0])
print(tup1[-1])

print(type(True))

print("--------------------------------")

set1 = set(["Geeks", "For", "Geeks"])
print(set1)

# loop through set
for i in set1:
    print(i)

# check if item exist in set
print("Geeks" in set1)

d = {}
dict1 = {1: "Geeks", 2: "For", 3: "all"}
print(dict1)
for i in dict1 :
    print(i)