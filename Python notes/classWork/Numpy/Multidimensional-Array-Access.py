import numpy as np
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

element = arr[0, 2]  # 3 - single element (row 0, column 2)
subarray = arr[0:2, 1:3]  # [[2, 3], [6, 7]] - rows 0-1, columns 1-2
subarray2 = arr[:, ::2]  # [[1, 3], [5, 7], [9, 11]] - all rows, every 2nd column

print("Element:", element)
print("Subarray:\n", subarray)
print("Subarray2:\n", subarray2)
