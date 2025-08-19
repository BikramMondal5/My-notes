#Class with __str__ method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Create object
p = Person("Alice", 30)

print(str(p))      # calls p.__str__()
