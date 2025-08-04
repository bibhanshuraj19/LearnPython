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