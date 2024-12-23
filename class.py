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