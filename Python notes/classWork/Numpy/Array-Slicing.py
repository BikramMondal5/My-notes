import numpy as np  

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[:5])    # [0, 1, 2, 3, 4] - first five elements
print(arr[5:])      # [5, 6, 7, 8, 9] - from index 5 to end
print(arr[::2])     # [0, 2, 4, 6, 8] - every second element

# Note:
# 1. Syntax: array[start:stop:step]
# 2. start is inclusive, stop is exclusive, step is optional