#5.1
#list

myList=[3,5,62,12,9]
max=max(myList)
min=min(myList)
print("max value in list is {}".format(max))
print("min value in list is {}".format(min))

#5.2
#dictionary

myDict1={"name":"arsh","age":25,"rollno.":1023}
print(myDict1["name"])

#5.3
#sort a list in asc and descending order

myList.sort()
print(myList)
myList.reverse()
print(myList)

#5.4
#merge two dictionaries

myDict2={"name":"sukh","age":25,"rollno.":1022}
myDict1.update(myDict2)
print(myDict1)