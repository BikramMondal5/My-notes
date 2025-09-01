import numpy as np

# Example matrix
A = np.array([[1, 2], [3, 4]])

# Inverse
A_inv = np.linalg.inv(A)

print("Matrix:\n", A)
print("Inverse:\n", A_inv)
