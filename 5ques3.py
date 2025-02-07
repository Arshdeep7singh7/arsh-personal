import numpy as np
import matplotlib.pyplot as plt
initials_ascii_sum = 65 + 66  # Replace with your initials' ASCII sum
X = initials_ascii_sum
sales = np.array([X, X + 50, X + 100, X + 150, X + 200])

# b) Personalized tax rate
tax_rate = ((X % 5) + 5) / 100
sales_with_tax = sales * (1 + tax_rate)
print("Sales after applying tax:", sales_with_tax)

# c) Sales adjustment based on discount
discounted_sales = np.where(sales < X + 100, sales * 0.95, sales * 0.90)
print("Discounted sales:", discounted_sales)

# d) Expanding sales data for multiple weeks
sales_weeks = np.tile(sales, (3, 1))  # Stack three weeks
week_increase = np.array([1.02**i for i in range(3)]).reshape(-1, 1)
weekly_sales_adjusted = sales_weeks * week_increase
print("Sales data with weekly adjustments:\n", weekly_sales_adjusted)