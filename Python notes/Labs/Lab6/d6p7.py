class Animal:
    def speak(self):
        print("Animal speaking...")
    
    def sound(self):
        print("Some generic sound")

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

    def sound(self):
        print("Dog sound: Bow Bow")

class Cat(Animal):
    def meow(self):
        print("Meow!")

    def sound(self):
        print("Cat sound: Meow Meow")

# Polymorphism function
def make_sound(animal):
    animal.sound()

# Usage
d = Dog()
c = Cat()

make_sound(d)  # Dog sound
make_sound(c)  # Cat sound
