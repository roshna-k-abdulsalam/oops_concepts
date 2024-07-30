"""
Here's an example to demonstrate class inheritance:
    - Define a base class called `Animal`
    - Define a derived class called `Dog` that inherits from Animal
    - Define another derived class called `Cat` that inherits from Animal

`NotImplementedError` : It is useful in designing abstract base classes where
certain methods are meant to be overridden by any subclass, ensuring a consistent 
interface across different implementations.
"""

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")


    def info(self):
        return f"{self.name} is a {self.species}"
    

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name=name, species="Dog")
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
        return f"{base_info}, and its color is {self.color}"


# Create instances of Dog and Cat
my_dog = Dog(name="Buddy", breed="Golden Retriever")
my_cat = Cat(name="Whiskers", color="Black")


# Access methods and attributes
print(my_dog.info()) # Output: Buddy is a Dog, and its breed is Golden Retriever
print(my_dog.make_sound()) # Output: Woof!

print(my_cat.info()) # Output: Whiskers is a Cat, and its color is Black
print(my_cat.make_sound()) # Output: Meow!


# Trying to create an instance of Animal and call make_sound will raise an error
generic_animal = Animal(name="Generic", species="Unknown")
print(generic_animal.make_sound()) # Raises NotImplementedError: Subclasses must implement this method
