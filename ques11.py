#11.1
import math
num=int(input("enter a number"))
root=math.sqrt(num)
print(f"square root is {root}")

#11.2

import datetime
print("today is ")
print(datetime.date.today())

#11.3

import os

directory_path = "."  

all_files = os.listdir(directory_path)

files = [file for file in all_files if os.path.isfile(os.path.join(directory_path, file))]

print("Files in directory:", files)
