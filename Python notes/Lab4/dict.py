# Create a function with an arguments, ** (double asterisk) before a parameter name. Send a comma separated list of key value pair to return a dictionary.

def create_profile(**kwargs):
	profile = {}
	for key, value in kwargs.items():
		profile[key] = value
	return profile

print(create_profile(name="Alice",age=30,job="Developer"))