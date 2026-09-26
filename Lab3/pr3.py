# Guess a Number

import random

# Generate a random number between 1 and 9
number = random.randint(1,9)

# The loop continues untill the user guesses correctly
while True:
    guess = int(input("Guess a number between 1 and 9: "))

    if guess == number:
        print("Well guessed!")
        break
    else:
        print("Wrong guess. Try again.")