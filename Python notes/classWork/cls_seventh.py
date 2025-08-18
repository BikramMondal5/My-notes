#Class to explain polymorphism

class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Polymorphism in action
def make_sound(animal):
    animal.sound()

make_sound(Dog())  # Output: Bark
make_sound(Cat())  # Output: Meow
