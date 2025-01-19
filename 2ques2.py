myTuple=(45,89.5,76,45.4,89,92,58,45)
max=max(myTuple)
print(f"max value is {max}")
print(myTuple.index(max))
min =min(myTuple)
print(f"lowest value is {min}")
co=myTuple.count(min)
print(f"it appears {co} times")
reverse=myTuple[::-1]
myList=list(myTuple)
print(f"the req list is {myList}")
search=76
if search in myTuple:
    findex=myTuple.index(search)
    print(f"number {search} is present at {findex}")
else:
    print(f"the number {search} is not present in the tuple")