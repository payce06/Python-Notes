import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("If your guess is within 5 of the number, you win!")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7  # Allow up to 7 attempts

    while attempts < max_attempts:
        try:
            # Take user input
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Make a guess: "))