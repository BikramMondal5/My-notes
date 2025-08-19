class Person:
    def __init__(self, name, age, address):
        self.__name = name        # private attribute
        self.__age = age          # private attribute
        self.__address = address  # private attribute

    # Getter methods
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    # Setter methods
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_address(self, address):
        self.__address = address

p = Person("Alice", 25, "Delhi")
print(p.get_name())  # ✅ Correct way
# print(p.__name)    # ❌ Error: Cannot access private variable directly
