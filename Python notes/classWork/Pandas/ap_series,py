import numpy as np

# Function to generate AP series
def ap_series(a, d, n):
    series = []
    for i in range(n):
        term = a + i * d
        series.append(term)
    return series

# Example: first term = 2, common difference = 3, number of terms = 10
ap_series = ap_series(2, 3, 10)
print(ap_series)
arr_ap =np.array(ap_series)
print("Sum of AP Series: ", np.sum(arr_ap))
print("Mean of AP Series: ", np.mean(arr_ap))
print("Standard Deviation of AP Series: ", np.std(arr_ap))
print("Variance of AP Series: ", np.var(arr_ap))


#one-liner version
a, d, n = 2, 5, 15
ap = [a + i*d for i in range(n)]
print(ap)

