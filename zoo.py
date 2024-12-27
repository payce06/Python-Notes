import random

# Animal class
class Animal:
    def __init__(self, name, species, age, health):
        self.name = name
        self.species = species
        self.age = age
        self.health = health

    def feed(self, food):
        print(f"{self.name} is eating {food}.")
        self.health += 10

    def check_health(self):
        if self.health >= 70:
            status = "healthy"
    elif 40 <= self.health < 70:
            status = "moderate"
        else:
            status = "poor"
        return status

    def __str__(self):
        health_status = self.check_health()
        return f"{self.name} ({self.species}), Age: {self.age}, Health: {self.health} ({health_status})"

# Zoo class
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal.name} to the zoo.")
    
    def remove_animal(self, animal_name):
        for animal in self.animals:
            if animal.name == animal_name:
                self.animals.remove(animal)
                print(f"Removed {animal.name} from the zoo.")
                return
        print(f"Animal with name {animal_name} not found.")

    def show_animals(self):
        print("\nAnimals in the Zoo:")
        for animal in self.animals:
            print(animal)

    def feed_all(self):
        for animal in self.animals:
            food = random.choice(["grass", "meat", "fruits"])
            animal.feed(food)
