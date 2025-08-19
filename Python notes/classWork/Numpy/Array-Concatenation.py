import numpy as np  

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Concatenate along rows (axis=0)
np.concatenate((a, b), axis=0)
# array([[1, 2], [3, 4], [5, 6], [7, 8]])

# Concatenate along columns (axis=1)
np.concatenate((a, b), axis=1)
# array([[1, 2, 5, 6], [3, 4, 7, 8]])

# Alternatives:
np.vstack((a, b))  # Vertical stack
np.hstack((a, b))  # Horizontal stack

# axis=0 concatenates vertically (along rows)
# axis=1 concatenates horizontally (along columns)
# vstack() and hstack() are convenient alternatives