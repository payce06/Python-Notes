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