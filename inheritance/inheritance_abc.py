"""
Abstract Base Class : In Python, abstract base classes (ABCs) are a way to define interfaces 
when creating a framework that relies on the consistent implementation of methods across multiple 
derived classes. They are part of the abc module, which stands for Abstract Base Classes. 
This module allows you to define abstract methods that derived classes must implement.

Here's how to use abstract base classes in Python:
    - Import the abc Module: You need to import ABC and abstractmethod from the abc module.
    - Define the Abstract Base Class: Create a class that inherits from ABC.
    - Define Abstract Methods: Use the @abstractmethod decorator to define methods that must be implemented by any subclass.
"""

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, species):
        self.name = name
        self.species =species

    
    @abstractmethod
    def make_sound(self):
        pass

    
    def info(self):
        return f"{self.name} is a {self.species}" \
        

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name=name, species='Dog')
        self.breed = breed


    def make_sound(self):
        return "Woof!"
        
    
    def info(self):
        base_info = super().info()
        return f"{base_info}, its breed is {self.breed}"
    

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name=name, species='Cat')
        self.color = color


    def make_sound(self):
        return "Meow!"
        
    
    def info(self):
        base_info = super().info()
        return f"{base_info}, its color is {self.color}"
    

# Create instances of Dog and Cat
my_dog = Dog(name="Buddy", breed="Golden Retriever")
my_cat = Cat(name="Whiskers", color="Black")


# Access methods and attributes
print(my_dog.info())  # Output: Buddy is a Dog, and its breed is Golden Retriever
print(my_dog.make_sound())  # Output: Woof!

print(my_cat.info())   # Output: Whiskers is a Cat, and its color is Black
print(my_cat.make_sound())  # Output: Meow!


# Trying to create an instance of Animal will raise an error
try:
    generic_animal = Animal(name="Generic", species="Unknown")
except TypeError as e:
    print(e) # Output: Can't instantiate abstract class Animal with abstract methods make_sound
