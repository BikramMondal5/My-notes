import numpy as np  

a = np.array([1, 2, 3, 4])
b = np.array([4, 2, 2, 4])
print(a == b)  # [False, True, False, True]
print(a > b)   # [False, False, True, False]
print(np.maximum(a, b))  # [4, 2, 3, 4]

# Note: 
# 1. Element-wise comparisons return boolean arrays
# 2. maximum() returns element-wise maximum