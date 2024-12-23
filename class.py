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

# Creating instances of derived classes
dog = DogInherited("Rex", "German Shepherd")
cat = Cat("Whiskers", "black")

# Accessing methods from derived classes
dog.speak()  # Output: Rex the German Shepherd says Woof!
cat.speak()  # Output: Whiskers the black cat says Meow!

# ==============================================================================

# Example 3: Demonstrating Method Overriding
# Inheritance allows derived classes to override methods from the parent class.

# Base class (parent class)
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.make} {self.model}")

# Derived class (child class)
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)  # Calling the parent class constructor
        self.doors = doors

    # Overriding the display_info method
    def display_info(self):
        print(f"Car: {self.make} {self.model} with {self.doors} doors")

# Derived class (another child class)
class Truck(Vehicle):
    def __init__(self, make, model, payload_capacity):
        super().__init__(make, model)  # Calling the parent class constructor
        self.payload_capacity = payload_capacity

        # Overriding the display_info method
    def display_info(self):
        print(f"Truck: {self.make} {self.model} with a payload capacity of {self.payload_capacity} kg")

# Creating instances of derived classes
car = Car("Toyota", "Camry", 4)
truck = Truck("Ford", "F-150", 3000)

# Accessing overridden methods
car.display_info()  # Output: Car: Toyota Camry with 4 doors
truck.display_info()  # Output: Truck: Ford F-150 with a payload capacity of 3000 kg

# ==============================================================================

# Example 4: Using the `super()` function
# The `super()` function allows us to call methods from the parent class in the derived class.