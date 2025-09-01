# In a numpy array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) print first two elements. last 5 element and every second element

import numpy as np

arr = np.arange(10)
print("First 2:", arr[:2])
print("Last 5:", arr[-5:])
print("Every 2nd:", arr[::2])
