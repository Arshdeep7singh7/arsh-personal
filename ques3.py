#3.1

a=int (input("enter any number\n"))
if a>0:
    print("a is positive")
elif a<0:
    print("a is negative")
else:
    print("a is zero")

#3.2

res="even" if a%2==0 else "odd"
# print("the given number is {}".format(res))
if a%2==0:
    print("a is even")
else :
    print("a is odd")
