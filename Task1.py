#"Guess the hidden Number Game"

import random

def guess_the_hidden_number():
    required_number = random.randint(1, 100)
    attempts = 7  

    print("Welcome to the 'Guess the Number' game..!")
    print("I put a number between 1 and 100. You have 7 attempts to guess it.")

    while attempts > 0:
        try:
            guess = int(input(f"Attempt {8 - attempts}: Enter your guess: "))

            if guess == required_number:
                print(f"Congratulations! You guessed the number {required_number} correctly!")
                break
            elif guess < required_number:
                print("Low number! Try a higher number.")
            elif guess > required_number:
                print("High number! Try a lower number.")

            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts left.")
            else:
                print(f"Sorry, you've run out all of your attempts! The correct number was {required_number}.")

        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 100.")

guess_the_hidden_number()