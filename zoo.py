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