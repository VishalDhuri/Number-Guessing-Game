
import random

# Number Guessing Game
print("===================================")
print("       NUMBER GUESSING GAME")
print("===================================")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("\nI have selected a number between 1 and 100.")
print("Can you guess the correct number?")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")

        elif guess < secret_number:
            print("Too low! Try a higher number.")

        elif guess > secret_number:
            print("Too high! Try a lower number.")

        else:
            print("\nCongratulations! You guessed it correctly!")
            print("The correct number was:", secret_number)
            print("Total attempts:", attempts)
            print("\nThanks for playing!")
            break

    except ValueError:
        print("Invalid input! Please enter a valid whole number.")
