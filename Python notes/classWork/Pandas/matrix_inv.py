import numpy as np

# Example matrix
A = np.array([[1, 2],
              [3, 4]])

# Compute inverse
A_inv = np.linalg.inv(A)

print("Original Matrix:\n", A)
print("Inverse Matrix:\n", A_inv)
