class Person:
    def __init__(self, name, age, address):
        self.__name = name
        self.__age = age
        self.__address = address

    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}, Address: {self.__address}"

p = Person("Alice", 25, "Delhi")
print(p)   # Calls __str__()
