# Example 1: Defining a simple class
class Dog:
    # Constructor to initialize object state
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable

    # Method to display dog information
    def bark(self):
        print(f"{self.name} says Woof!")

    # Method to display the dog's age
    def get_age(self):
        print(f"{self.name} is {self.age} years old.")

# Creating an instance of the Dog class
my_dog = Dog("Buddy", 3)


# Accessing object methods
my_dog.bark()  # Output: Buddy says Woof!
my_dog.get_age()  # Output: Buddy is 3 years old.

# ==============================================================================
# Example 2: Inheritance
# Inheritance allows us to define a class that inherits methods and attributes from another class.

# Base class (parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


# Derived class (child class)
class DogInherited(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calling the parent class constructor
        self.breed = breed

    # Overriding the speak method
    def speak(self):
        print(f"{self.name} the {self.breed} says Woof!")

# Derived class (another child class)
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Calling the parent class constructor
        self.color = color

    # Overriding the speak method
    def speak(self):
        print(f"{self.name} the {self.color} cat says Meow!")