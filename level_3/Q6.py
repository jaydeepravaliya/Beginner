# Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal): 
    def speak(self):
        print("Woof!")

# Multiple Inheritance
class Flyable:
    def fly(self):
        print("Can fly")

class Swimmable:
    def swim(self):
        print("Can swim")

class Bird(Animal, Flyable):
    def __init__(self, name):
      super().__init__(name)

    def speak(self):
        print("Chirp!")

# Multilevel Inheritance
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

    def give_birth(self):
        print("Gives birth to live young")


class Bat(Mammal, Flyable):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Screech!")
