import numpy as np

# Recursive Fibonacci function
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# Generate Fibonacci series for n terms
n = 10
fib_series = [fib(i) for i in range(n)]

# Stats using numpy
sum_fib = np.sum(fib_series)
mean_fib = np.mean(fib_series)
var_fib = np.var(fib_series)
std_fib = np.std(fib_series)

print("Fibonacci Series:", fib_series)
print("Sum:", sum_fib, "Mean:", mean_fib, "Variance:", var_fib, "Std Dev:", std_fib)
