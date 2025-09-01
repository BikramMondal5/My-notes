import numpy as np

class MathSeries:

    def fibonacci(self, n):
        def fib(num):
            if num <= 1:
                return num
            return fib(num-1) + fib(num-2)

        series = [fib(i) for i in range(n)]
        return self.stats(series)

    def ap(self, a, d, n):
        series = [a + (i-1)*d for i in range(1, n+1)]
        return self.stats(series)

    def matrix_inverse(self, mat):
        return np.linalg.inv(mat)

    def stats(self, series):
        return {
            "series": series,
            "sum": np.sum(series),
            "mean": np.mean(series),
            "variance": np.var(series),
            "std_dev": np.std(series)
        }

# Usage
ms = MathSeries()
print("Fibonacci:", ms.fibonacci(10))
print("AP:", ms.ap(2, 3, 10))
print("Matrix Inverse:\n", ms.matrix_inverse(np.array([[1, 2], [3, 4]])))
