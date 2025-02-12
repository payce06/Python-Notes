import random

class Player:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_enemy(self):
        return random.randint(1, self.attack)
       
class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_player(self):
        return random.randint(1, self.attack)

def battle(player, enemy):
    print(f"A wild {enemy.name} has appeared!")
    while player.is_alive() and enemy.is_alive():
        action = input("Do you want to (A)ttack or (F)lee? ").lower()
       
        if action == 'a':
            player_damage = player.attack_enemy()
            enemy.take_damage(player_damage)
            print(f"You attack {enemy.name} and deal {player_damage} damage.")
           
            if enemy.is_alive():
                enemy_damage = enemy.attack_player()
                player.take_damage(enemy_damage)
                print(f"{enemy.name} attacks you and deals {enemy_damage} damage.")
        elif action == 'f':
            print("You flee the battle!")
            break
        else:
            print("Invalid action. Please choose again.")

        print(f"\nYour Health: {player.health} | {enemy.name}'s Health: {enemy.health}")

    if player.is_alive() and not enemy.is_alive():
        print(f"You defeated the {enemy.name}!")
    elif not player.is_alive():
        print(f"You have been defeated by {enemy.name}... Game Over!")

def explore(player):
    print("\nYou are exploring the dungeon...")
    while player.is_alive():
        print("\nYou come across a door.")
        choice = input("Do you want to (E)nter the door or (L)eave the dungeon? ").lower()
       
        if choice == 'e':
            enemy_name = random.choice(["Goblin", "Orc", "Dragon"])
            enemy_health = random.randint(30, 100)
            enemy_attack = random.randint(5, 20)
            enemy = Enemy(enemy_name, enemy_health, enemy_attack)
            battle(player, enemy)
           
            if not player.is_alive():
                break
        elif choice == 'l':
            print("You leave the dungeon. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

def main():
    print("Welcome to the Dungeon Adventure Game!")
    player_name = input("Enter your character's name: ")
    player = Player(player_name, 100, 15)  # Player with 100 health and 15 attack
    explore(player)

if __name__ == "__main__":
    main()