# Write a function to find the farhenheit temperature for a given celsius 

def celsius_to_fahrenheit(celsius):
	fahrenheit = (celsius * 9/5) + 32    
	return fahrenheit
# Function call examples
print(celsius_to_fahrenheit(0))    
# Output: 32.0
print(celsius_to_fahrenheit(100))  
# Output: 212.0