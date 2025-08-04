# Create a function to recursively calculate the factorial of an input number.

def factorial(n): 
	# Base case: if n is 1, return 1 
	if n == 1: 
		return 1 
	# Recursive case: n * factorial of (n-1) 
	else: return n * factorial(n-1)
print(factorial(5))