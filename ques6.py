#6.1 
#no. of vowels
name="arshdeep singh"
count =0
for i in name:
    if i=='a'or i=='e' or i=='i'or i=='o' or i=='u':
        count+=1
    else:
        continue
print (count)

#6.2

reverseString=name[::-1]
print(reverseString)

#6.3

check=str(input("enter any string\n"))
reverseCheck=check[::-1]
if check==reverseCheck:
    print("it is a palindrome")
else:
    print("not a palindrome")
  