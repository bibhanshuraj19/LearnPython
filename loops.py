primes = [2,3,5,7]
for prime in primes :
    print(prime)

for x in range(5) :
    print(x)
for x in range(3,8) :
    print(x)

range1 = []
for x in range(3,8,2) :
    range1.append(x)
    print(range1)

count = 0
while count < 5 :
    print(count)
    count += 1

# This prints out 0,1,2,3,4
count1 = 0
while True :
    print(count1)
    count1 += 1
    if count1 >= 5 :
        break

# This prints only odd numbers
for x in range(10) :
    if x % 2 == 0 :
        continue
    print(x)

count2 = 0
while(count2 < 5):
    print(count2)
    count2 += 1
else :
    print("Count have reached %d"%(count2))


for i in range (1,10):
    if i % 5 == 0:
        break
    print(i)
else :
    print("this is not a loop")

print("------------------------------------------------")
n = 6
for i in range(1,n) :
    print(i)
print("------------------------------------------------")


l1 = ["geeks", "for", "geeks"]
for i in l1 :
    print(i)
print("------------------------------------------------")

tup = ("geeks", "for", "geeks")
for i in tup :
    print(i)
print("------------------------------------------------")

s = "geeks"
for i in s :
    print(i)
print("------------------------------------------------")

d = dict({'x':123, 'y':456})
for i in d:
    print("%s : %d" %(i, d[i]))
print("------------------------------------------------")

set1 = {1,2,3,4,5,6,7,8,9,10}
for i in set1 :
    print(i)
print("------------------------------------------------")

li = ["geeks", "for", "geeks", "for", "me"]
for index in range(len(li)) :
    print(li[index])
print("------------------------------------------------")


li1 = ["geeks", "for", "geeks", "for", "me"]
for index in range(len(li1)) :
    print(li1[index])
else :
    print("this is not a loop")
print("------------------------------------------------")

cnt = 0
while (cnt < 5) :
    cnt = cnt + 1
    print("hello")
print("-------------------------------------------------")

cnt = 0
while (cnt < 5) :
    cnt = cnt + 1
    print("hello")
else :
    print("this is not a loop")
print("-------------------------------------------------")

for i in range(1,5) :
    for j in range (i) :
        print(i, end=' ')
    print()
print("-------------------------------------------------")

for letter in "bibhanshuraj" :
    if letter == 'a' or letter == 'b' :
        continue
    print(letter)
print("-------------------------------------------------")
for letter in "bibhanshuraj" :
    if letter == 'b' or letter == 'a' :
        break
print(letter)
print("-------------------------------------------------")

for letter in "bibhanshuraj" :
    pass
print(letter)  # iterates through all and prints the last one
print("-------------------------------------------------")

