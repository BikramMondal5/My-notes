# Parent class
class Animal:
    def speak(self):
        print("This animal makes a sound")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Using inheritance
d = Dog()
d.speak()   # Inherited from Animal
d.bark()    # Defined in Dog
