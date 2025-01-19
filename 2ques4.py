setA={34,56,78,90}
setB={78,45,90,23}
num=setA.union(setB)
print(f"union of both sets is {num}")
comm=setA.intersection(setB)
print(f"commmon scores are {comm}")
diff=setA.difference(setB)
print(f"scores exclusive to b are {diff}")
diff1=setB.difference(setA)
print(f"scores exclusive to a are {diff1}")
if setA.issubset(setB):
    print("a is subset of b")
else:
    print("a is not subset of b")
if setB.issuperset(setA):
    print("b is superset of a")
else:
    print("b is not superset of a")
num=int(input("enter the number you want to delete from a"))
if num in setA:
    setA.remove(num)
    print("number is deleted")
else:
        print("number is  not present")
print(f"updated set {setA}")