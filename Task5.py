# "Word Scramble Game"

import random

fruit_list = ["banana", "apple" , "pomegrante", "mango", "peach", "pineapple", "orange", "waterlemon", "pear", "cherry", "papaya", "melon"]

original_fruitword = random.choice(fruit_list)

scrambled_fruitword = ''.join(random.sample(original_fruitword, len(original_fruitword)))

attempts = 5

print("Welcome to the Word Scramble Game!")
print(f"Try to guess the original fruit word from the scrambled word: {scrambled_fruitword}")
print(f"You have {attempts} attempts.\n")

while attempts > 0:
    pl_guess = input("Enter your guess: ").strip()

    if not pl_guess:
        print("Invalid input! Please enter a word.\n")
        continue

    if pl_guess.lower() == original_fruitword:
        print("Congratulations! You guessed the correct word!")
        break

    attempts -= 1
    if attempts > 0:
        print(f"Incorrect! Try again. You have {attempts} attempts left.\n")
    else:
        print(f"You're out of attempts! The correct word was: {original_fruitword}")