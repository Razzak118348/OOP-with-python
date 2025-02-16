#  Simple inheritance example
# class Animal:
#     def speak(self):
#         return "Animal makes a sound"

# class Dog(Animal):
#     def bark(self):
#         return "Dog barks"

# dog = Dog()
# print(dog.speak())  # Inherited method
# print(dog.bark())   # Child class method


# Multiple Inheritance
# class Animal:
#     def speak(self):
#         return "Animal makes a sound"

# class Walker:
#     def walk(self):
#         return "Animal walks"

# class Dog(Animal,Walker):
#     def bark(self):
#         return "Dog barks"

# dog=Dog()
# print(dog.speak())
# print(dog.walk())
# print(dog.bark())

# mULTILEVEL INHERITANCE

class Animal:
    def breathe(self):
        return "Animal breathes"

class Mammal(Animal):
    def feed_milk(self):
        return "Mammal feeds milk"

class Dog(Mammal):
    def bark(self):
        return "Dog barks"

dog = Dog()
print(dog.breathe())   # Inherited from Animal
print(dog.feed_milk()) # Inherited from Mammal
print(dog.bark())      # Own method


# using super() method
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling parent constructor
        self.breed = breed

    def speak(self):
        return f"{self.name}, a {self.breed}, barks"

dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Buddy, a Golden Retriever, barks
