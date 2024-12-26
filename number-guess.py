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
           
            # Check the guess
            if guess == secret_number:
                print(f"Congratulations! You guessed the exact number in {attempts + 1} attempts!")
                break
            elif abs(guess - secret_number) <= 5:
                print(f"Great job! Your guess {guess} is within 5 of the correct number ({secret_number}). You win!")
                break
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
           
            attempts += 1
        except ValueError:
            print("Please enter a valid number.")
   
    # If the user runs out of attempts
    if attempts == max_attempts and abs(guess - secret_number) > 5:
        print(f"Sorry, you've used all your attempts. The correct number was {secret_number}.")
   
    # Ask to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing! Goodbye!")

# Run the game
if __name__ == "__main__":
    play_game()
