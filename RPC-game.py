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
                player_move = moves[player_input]
            # Computer's move
            computer_move = moves[random.randint(1, 3)]
           
            print(f"You chose: {player_move}")
            print(f"The computer chose: {computer_move}")

            # Determine the winner of the round
            if player_move == computer_move:
                print("It's a tie!")
            elif (
                (player_move == "rock" and computer_move == "scissors") or
                (player_move == "paper" and computer_move == "rock") or
                (player_move == "scissors" and computer_move == "paper")
            ):
                print("You win this round!")
                player_score += 1
            else:
                print("Computer wins this round!")
                computer_score += 1

            print(f"Score: You {player_score} - {computer_score} Computer\n")
       
        except ValueError:
            print("Invalid input! Please enter a number (1, 2, or 3).")
            continue