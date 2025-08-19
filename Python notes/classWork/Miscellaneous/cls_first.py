#Create a class and create an object to instantiate the class
class Dog:
    species = "Canine"  # Class attribute, public variable
    
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
        
# Creating an object
dog1 = Dog("Buddy", 3)
print(dog1.name)     # Output: Buddy
print(dog1.species)  # Output: Canine
