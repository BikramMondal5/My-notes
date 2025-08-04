# Write a function greet with default parameter greeting="Hello" and parameter name and test it in venv with default parameter and with a given parameter for greeting. 

def greet(name, greeting="Hello"):    
	return f"{greeting}, {name}!"    
print(greet("Alice"))         # "Hello, Alice!“
print(greet("Bob", "Hi"))      # "Hi, Bob!"