import numpy as np

arr = np.arange(16).reshape(4, 4)

# Split into 2 equal arrays horizontally
print(np.split(arr, 2, axis=0))

# Split at specific indices
print(np.split(arr, [1, 3], axis=1))

# Note: 
# 1. Split arrays into multiple subarrays
# 2. Can split equally or at specific indices
# 3. Specify axis for split direction