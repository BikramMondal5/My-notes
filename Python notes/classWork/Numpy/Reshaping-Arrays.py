import numpy as np

arr = np.arange(12)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Reshape to 3×4
print(arr.reshape(3, 4))
# array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])

# Reshape to 2×2×3
print(arr.reshape(2, 2, 3))

# Note: 
# 1. Changes array shape without changing data
# 2. New shape must have same total number of elements