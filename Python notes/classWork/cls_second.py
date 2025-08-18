#class with private variabless

class Person:
    def __init__(self, name, age,address):
        self.name = name  # Instance variable
        self.age = age    # Instance variable
        self.__address = address

# Creating an object
p1 = Person("Alice", 30, 'XXXX')

print(p1.name)  # Output: Alice
print(p1.age)   # Output: 30
print(p1.__address)