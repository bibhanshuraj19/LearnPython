tuple1 = ("apple", "banana", "mango", "cherry", "apple", "cherry")
print(tuple1)

tuple2 = ("apple", "banana", "mango", "cherry", "apple", "cherry")
print(len(tuple2)) 

tuple3 = ("apple", "banana", "mango", "cherry", "apple", "cherry")
print(type(tuple3))

tuple4 = ("apple")
print(type(tuple4))  # not a tuple but a string

tuple4 = ("apple", "banana", "mango", "cherry", "apple", "cherry")
print(tuple4[1])

tuple5 = ("apple", "banana", "mango", "cherry", "apple", "cherry")
if "apple" in tuple5:
    print("yeah apple is available")

tuple6 = ("apple", "banana", "mango", "cherry", "apple", "cherry")
tuple7 = list(tuple6)
tuple7[1] = "Kiwi"
tuple6 = tuple(tuple7)
print(tuple6)

tuple8 = ("apple", "banana", "mango", "cherry", "apple", "cherry")
tuple9 = list(tuple8)
tuple9.append("mausami")
tuple8 = tuple(tuple9)
print(tuple8)

tuple10 = ("apple", "banana", "mango", "cherry", "apple", "cherry")
for x in tuple10:
    print(x)

tuple11 = ("potato", "tomato", "cabbage", "pickle", "onion", "finger")
for x in range(len(tuple10)):
    print(tuple11[x])

tuple12 = ("potato1", "tomato1", "cabbage1", "pickle1", "onion1", "finger1")
i = 0
while i < len(tuple12):
    print(tuple12[i])
    i = i + 1
print("----------------------------------------------------")
tup = ()
print(tup)

tup = ('Geeks','For')
print(tup)

li = [1,2,3,4,5]
print(tuple(li))

tup = tuple('Geeks')
print(tup)