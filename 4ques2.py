import numpy as np
arr=np.array([1,2,3,6,4,5])
print(arr[::-1])

# part 2

x=np.array([1,2,3,4,5,1,2,1,1,1])
y=np.array([1,1,1,2,3,4,2,4,3,3,1])

most_frequent = np.bincount(x).argmax()
first_index = np.where(x == most_frequent)[0][0]
most_frequent1 = np.bincount(y).argmax()
first_index1 = np.where(y == most_frequent)[0][0]

print("Most frequent element in x:", most_frequent)
print("Index of first occurrence in x:", first_index)
print("Most frequent element in y:", most_frequent1)
print("Index of first occurrence in y:", first_index1)
