import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Min:", arr.min())
print("Max:", arr.max())
print("Mean:", arr.mean())
print("Median:", np.median(arr))
print("Std Dev:", arr.std())
print("Variance:", arr.var())
print("Sum:", arr.sum())

print("\nRow-wise sum:", arr.sum(axis=1))
print("Column-wise sum:", arr.sum(axis=0))
