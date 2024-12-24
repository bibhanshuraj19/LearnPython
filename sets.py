thisset = {"apple", "banana", "cherry"}
print(thisset)
print(len(thisset))
print(type(thisset))

thisset1 = {"apple", "banana", "cherry","apple"}
print(thisset1)

thisset2 = {"apple", "banana", "cherry", True, 1, 2}
print(thisset2)

thisset3 = {"apple", "banana", "cherry", True, 1, 2, False, 0, 3}
print(thisset3)

thisset4 = (("apple", "banana", "cherry"))
print(thisset4)

thisset5 = {"apple", "banana", "cherry"}
for x in thisset5:
    print(x)

thisset6 = {"apple", "banana", "cherry", True, 1, 2}
print("banana" in thisset6)

thisset7 = {"apple", "banana", "cherry", True, 1, 2}
print("banana" not in thisset7)

thisset8 = {"apple", "banana", "cherry", True, 1, 2}
thisset8.add("orange")
print(thisset8)

