fruits1 = ['apple','mango','banana','guava']
fruits1.append('ice')
print(fruits1)

fruits2 = ['apple','mango','banana','guava']
fruits2.insert(0,'cream')
print(fruits2)

fruits3 = ['apple','mango','banana','guava']
tropical = ['apple2','mango2']
fruits3.extend(tropical)
print(fruits3)

fruits4 = ['apple','mango','banana','guava']
fruits4.remove("banana")
print(fruits4)

fruits5 = ['apple','mango','banana','guava']
fruits5.pop(1)
print(fruits5)

fruits6 = ['apple','mango','banana','guava']
del fruits6[1:3]
print(fruits6)

fruits7 = ['apple','mango','banana','guava']
fruits7.clear()
print(fruits7)

fruits8 = ['apple','mango','banana','guava']
for fruits in fruits8:
    print(fruits)

fruits9 = ['apple','mango','banana','guava']
for i in range(len(fruits9)):
    print([i])

fruits10 = ['apple','mango','banana','guava']
i = 0
while i < len(fruits10) :
    print(fruits10[i])
    i = i + 1

fruits11 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits11:
    if 'a' in x:
        newlist.append(x)
    print(newlist)

fruits12 = ["mango", "cherry", "banana", "kiwi", "apple"]
fruits12.sort()
print(fruits12)

fruits13 = ["mango", "cherry", "banana", "kiwi", "apple"]
fruits13.sort(reverse=True)
print(fruits13)

def myfunc(num):
    return abs(num - 50)
numbers = [100, 200, 300, 400, 500, 600]
numbers.sort(key=myfunc)
print(numbers)

fruits14 = ["mango", "cherry", "banana", "kiwi", "apple"]
fruits15 = fruits14.copy()
print(fruits15)

fruits16 = ["mango", "cherry", "banana", "kiwi", "jamun"]
fruits17 = fruits16[:]
print(fruits17)

fruits18 = ["mango", "cherry", "banana", "kiwi", "apple"]
fruits19 = ["guava", "litchi", "adrak"]
fruits20 = fruits18 + fruits19
print(fruits20)

fruits21 = ["mango", "cherry", "banana", "kiwi", "apple"]
fruits22 = ["guava", "litchi", "adrak", "aaloo"]
for x in fruits22:
    fruits21.append(x) 
print(fruits21)

fruits23 = ["mango", "cherry", "banana", "kiwi", "apple"]
fruits24 = ["guava", "litchi", "adrak", "tomato"]
fruits23.extend(fruits24)
print(fruits23)