import numpy as np
import matplotlib.pyplot as plt
array_a = np.array([10, 52, 62, 16, 16, 54, 453])

# i. Sorted array
sorted_array = np.sort(array_a)
print("Sorted array:", sorted_array)

# ii. Indices of sorted array
sorted_indices = np.argsort(array_a)
print("Indices of sorted array:", sorted_indices)

# iii. 4 smallest elements
smallest_4 = np.sort(array_a)[:4]
print("4 smallest elements:", smallest_4)

# iv. 5 largest elements
largest_5 = np.sort(array_a)[-5:]
print("5 largest elements:", largest_5)

# Q2(b): Array filtering
array_b = np.array([1.0, 1.2, 2.2, 2.0, 3.0, 2.0])

# i. Integer elements only
integer_elements = array_b[array_b == array_b.astype(int)]
print("Integer elements only:", integer_elements)

# ii. Float elements only
float_elements = array_b[array_b != array_b.astype(int)]
print("Float elements only:", float_elements)
