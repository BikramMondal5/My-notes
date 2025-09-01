import numpy as np

# AP parameters
a = 2   # first term
d = 3   # common difference
n = 10  # number of terms

# Generate AP series
ap_series = [a + (i-1)*d for i in range(1, n+1)]

# Stats
sum_ap = np.sum(ap_series)
mean_ap = np.mean(ap_series)
var_ap = np.var(ap_series)
std_ap = np.std(ap_series)

print("AP Series:", ap_series)
print("Sum:", sum_ap, "Mean:", mean_ap, "Variance:", var_ap, "Std Dev:", std_ap)
