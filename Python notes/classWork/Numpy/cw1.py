# First install the dependency
import numpy as np

# create a 1D array
arr = np.array([1,2,3,4])
print(arr)

# create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)

# Zero arrays
np_zero = np.zeros((2, 3))  # 2 rows, 3 columns
print(np_zero)

# one array
np_one = np.ones((2, 3))  # 2 rows, 3 columns
print(np_one)

print(arr[2])
print(arr[:2])
print(arr[::2])
