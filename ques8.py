try:
    num=int(input("enter a number"))
    res=10/num
except ZeroDivisionError:
    print("zero divion error occurred")
except ValueError:
    print("enter a valid input")

#8.3

try:
    num=int(input("enter a number"))
    res=10/num
except ZeroDivisionError:
    print("zero divion error occurred")
except ValueError:
    print("enter a valid input")
finally:
    print("this will always run")