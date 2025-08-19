import numpy as np

arr = np.array([10, 20, 30, 40, 50])
first = arr[0]   # 10
last = arr[-1]   # 50
third = arr[2]   # 30

print("First:", first)
print("Last:", last)
print("Third:", third)

# Note: 
# 1. Use positive indices to access elements from the start
# 2. Use negative indices to access elements from the end
# 3. Much faster than Python list indexing