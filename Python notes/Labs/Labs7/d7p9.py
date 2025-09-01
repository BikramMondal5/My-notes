import time
import numpy as np

# Using loop
n = 10_000_000
a = np.arange(n)
b = np.arange(n)

start = time.time()
result_loop = np.zeros(n)
for i in range(n):
    result_loop[i] = a[i] + b[i]
end = time.time()
loop_time = end - start

# Using vectorization
start = time.time()
result_vec = a + b
end = time.time()
vec_time = end - start

print("Loop time:", loop_time)
print("Vectorized time:", vec_time)
print("Speedup:", loop_time / vec_time)
