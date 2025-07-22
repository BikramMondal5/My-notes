def create_profile(**kwargs):
	profile = {}
	for key, value in kwargs.items():
		profile[key] = value
	return profile

print(create_profile(name="Alice",age=30,job='Full-stack developer'))