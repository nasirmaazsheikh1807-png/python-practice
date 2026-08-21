from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
class Cat(Animal):
    def sound(self):
        print("Cat Meows")
class Cow(Animal):
    def sound(self):
        print("Cow Moos")

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.sound()