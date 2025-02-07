import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)

# Y = x^2
y1 = x**2
plt.plot(x, y1, label="Y = x^2")

# Y = sin(x)
y2 = np.sin(x)
plt.plot(x, y2, label="Y = sin(x)")

# Y = e^x
y3 = np.exp(x)
plt.plot(x, y3, label="Y = e^x")

# Y = log(|x| + 1)
y4 = np.log(np.abs(x) + 1)
plt.plot(x, y4, label="Y = log(|x| + 1)")

# Add title, labels, and grid
plt.title("Function Plots")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.legend()
plt.grid(True)

plt.show()