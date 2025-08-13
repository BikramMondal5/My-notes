import numpy as np

# Create a 1D array from a list
arr1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1d)

# Create a 2D array (matrix) from nested lists
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2d)

# Create an array filled with zeros
zeros_array = np.zeros((2, 3)) # 2 rows, 3 columns
print("\nZeros Array:\n", zeros_array)

# Create an array filled with ones
ones_array = np.ones((3, 2)) # 3 rows, 2 columns
print("\nOnes Array:\n", ones_array)

# Create an array with a range of values
range_array = np.arange(0, 10, 2) # Start, Stop (exclusive), Step
print("\nRange Array:", range_array)