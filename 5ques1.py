import numpy as np
import matplotlib.pyplot as plt
gfg = np.matrix('[4, 1, 9; 12, 3, 1; 4, 5, 6]')

# i. Sum of all elements
sum_all_elements = np.sum(gfg)
print("Sum of all elements:", sum_all_elements)

# ii. Sum of all elements row-wise
sum_row_wise = np.sum(gfg, axis=1)
print("Sum row-wise:", sum_row_wise)

# iii. Sum of all elements column-wise
sum_column_wise = np.sum(gfg, axis=0)
print("Sum column-wise:", sum_column_wise)