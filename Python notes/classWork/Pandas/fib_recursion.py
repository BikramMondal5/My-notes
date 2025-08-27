import numpy as np
def fibonacci_series(n):
    """
    Generates a Fibonacci series up to n terms using recursion.

    Args:
        n (int): The number of terms in the Fibonacci series.

    Returns:
        list: A list containing the Fibonacci series.
    """
    def fib_recursive(k):
        if k == 0:
            return 0
        elif k == 1:
            return 1
        else:
            return fib_recursive(k - 1) + fib_recursive(k - 2)

    if n <= 0:
        return []
    else:
        return [fib_recursive(i) for i in range(n)]

if __name__ == "__main__":
    num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
    fib_series = fibonacci_series(num_terms)
    print(f"Fibonacci series up to {num_terms} terms: {fib_series}")
    arr_fib = np.array(fib_series)

    print("Sum of Fibonacci Series: ", np.sum(arr_fib))
    print("Mean of Fibonacci Series: ", np.mean(arr_fib))
    print("Standard Deviation of Fibonacci Series: ", np.std(arr_fib))
    print("Variance of Fibonacci Series: ", np.var(arr_fib))