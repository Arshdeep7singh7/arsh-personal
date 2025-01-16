#4.1

print("using for loop")
for i in range(1,11):
    print(i)

#4.2

print("using while loop")

i=1
while i<11:
    print(i)
    i=i+1

#4.3
#sum of numbers from 1 to 100
sum=0
for i in range(1,101):
    sum+=i
print("the req sum is {}".format(sum))