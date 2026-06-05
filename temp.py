import numpy as np
import matplotlib.pyplot as plt

# Example unsorted data
x1 = np.array([10, 20, 30])
y1 = np.array([1, 2, 3])

x2 = np.array([15, 25, 5])
y2 = np.array([4, 5, 6])

# Sort x1 and y1
idx1 = np.argsort(x1)
x1_sorted, y1_sorted = x1[idx1], y1[idx1]

# Sort x2 and y2
idx2 = np.argsort(x2)
x2_sorted, y2_sorted = x2[idx2], y2[idx2]

# Plot sorted data
plt.plot(x1_sorted, y1_sorted, label='Line 1')
plt.plot(x2_sorted, y2_sorted, label='Line 2')
plt.legend()
plt.show()   