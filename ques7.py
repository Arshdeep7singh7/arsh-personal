#7.1

file=open("first.txt",'r+')
file.write("hello arsh!")
content=file.read()
print(content)
file.close()
#7.2

file=open("first.txt",'a+')
file.write("\n new line added")
res=file.read()
print (res)
file.close()
#7.3

file=open("first.txt",'r')
lens=file.readlines()
count=len(lens)
print(count)
file.close()