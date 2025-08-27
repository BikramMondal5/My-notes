def fibonacci_series(n):
    """
    Generates a Fibonacci series up to n terms.

    Args:
        n (int): The number of terms in the Fibonacci series.

    Returns:
        list: A list containing the Fibonacci series.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        series = [0, 1]
        while len(series) < n:
            next_term = series[-1] + series[-2]
            series.append(next_term)
        return series

if __name__ == "__main__":
    num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
    fib_series = fibonacci_series(num_terms)
    print(f"Fibonacci series up to {num_terms} terms: {fib_series}")
