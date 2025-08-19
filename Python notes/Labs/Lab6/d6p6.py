class Animal:
    def speak(self):
        print("Animal speaking...")

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

# Usage
d = Dog()
d.speak()  # From parent
d.bark()   # From child
