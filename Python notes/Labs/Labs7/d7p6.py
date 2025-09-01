import numpy as np

arr = np.arange(16).reshape(4, 4)

# Split horizontally (row-wise)
print("Horizontal split:\n", np.hsplit(arr, 2))

# Split vertically (column-wise)
print("Vertical split:\n", np.vsplit(arr, 2))
