# Write a function which takes an array and returns the sum of all the elements in array.

def sum_all(*args):    
	total = 0    
	for num in args:        
		total += num    
	return total    

print(sum_all(1, 2, 3, 4)) 