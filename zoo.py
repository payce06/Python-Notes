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


    def check_all_health(self):
        print("\nHealth Status of All Animals:")
        for animal in self.animals:
            print(f"{animal.name} is {animal.check_health()}.")

# Zookeeper class
class Zookeeper:
    def __init__(self, name):
        self.name = name

    def feed_animal(self, animal, food):
        print(f"{self.name} is feeding {animal.name} with {food}.")
        animal.feed(food)

    def check_animal_health(self, animal):
        health_status = animal.check_health()
        print(f"{self.name} checked {animal.name}'s health: {health_status}.")
    
    # Main function
def main():
    print("Welcome to the Zoo Management System!")
    zoo = Zoo("Sunnyvale Zoo")

    # Creating animals
    lion = Animal("Leo", "Lion", 5, 80)
    elephant = Animal("Dumbo", "Elephant", 10, 60)
    giraffe = Animal("Ginny", "Giraffe", 7, 50)

    # Adding animals to the zoo
    zoo.add_animal(lion)
    zoo.add_animal(elephant)
    zoo.add_animal(giraffe)

    # Creating a zookeeper
    zookeeper = Zookeeper("Jake")

    # Menu loop
    while True:
    
    
        print("\nMenu:")
        print("1. Show Animals")
        print("2. Add Animal")
        print("3. Remove Animal")
        print("4. Feed All Animals")
        print("5. Feed Specific Animal")
        print("6. Check Health of All Animals")
        print("7. Check Health of Specific Animal")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            zoo.show_animals()
        elif choice == "2":
            name = input("Enter animal name: ")
            species = input("Enter animal species: ")
            age = int(input("Enter animal age: "))
            health = int(input("Enter animal health (0-100): "))
            new_animal = Animal(name, species, age, health)
            zoo.add_animal(new_animal)
        elif choice == "3":
            name = input("Enter the name of the animal to remove: ")
            zoo.remove_animal(name)
        elif choice == "4":