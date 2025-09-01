import numpy as np

# Transition matrix
P = np.array([[0.7, 0.3],
              [0.4, 0.6]])

# Solve (pi * P = pi), i.e., (P^T - I)*pi = 0
# Add the condition that sum(pi) = 1

# Transpose and subtract I
A = P.T - np.eye(2)

# Add normalization equation
A = np.vstack([A, np.ones(2)])
b = np.array([0, 0, 1])

# Solve least squares
pi, _, _, _ = np.linalg.lstsq(A, b, rcond=None)

print("Stationary distribution:", pi)
