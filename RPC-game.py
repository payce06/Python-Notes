import random

def play_game():
    print("Welcome to Rock, Paper, Scissors: Best of Five!")
    print("Enter 1 for Rock, 2 for Paper, 3 for Scissors.")
    print("Let's see who wins the most out of five rounds!\n")

    # Mapping numbers to moves
    moves = {1: "rock", 2: "paper", 3: "scissors"}

    player_score = 0
    computer_score = 0
    rounds = 5

    for round_number in range(1, rounds + 1):
        print(f"Round {round_number}!")
        try:
            # Get the player's move
            player_input = int(input("Your move (1: Rock, 2: Paper, 3: Scissors): "))
            if player_input not in moves:
                print("Invalid input! Please enter 1, 2, or 3.")
                continue