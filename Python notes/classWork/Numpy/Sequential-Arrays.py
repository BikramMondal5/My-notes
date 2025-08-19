import numpy as np

seq1 = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
seq2 = np.linspace(0, 1, 5)  # 5 evenly spaced points

print(seq1)
print(seq2)

# Note:
# 1. arange(start, stop, step) creates sequences with step intervals
# 2. linspace(start, stop, num) creates evenly spaced points