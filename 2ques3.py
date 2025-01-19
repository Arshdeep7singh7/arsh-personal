import random
myList= [random.randint(100, 900) for _ in range(100)]
print(myList)
count=0
count1=0
count2=0
list1=[]
list2=[]
list3=[]
for i in myList:
    if i%2==0:
        count+=1
        list1.append(i)
print(f"number of evens are {count}")
print(f"list is {list1}")
for i in myList:
    if i%2!=0:
        count1+=1
        list2.append(i)
print(f"number of odds are {count1}")
print(f"list is {list2}")
check=True
for j in myList:
    for num in range(2,int(j/2)):
        if j%num==0:
            check=False
            break
    if check:
        list3.append(j)
        count2+=1
        
print(f"number of primes are {count2}")
print(f"list is {list3}")