""" 
Exercise 1
"""

import random

LOW = 0
HIGH = 100


def guessing_game() -> None:
    number: int = random.randint(LOW, HIGH)

    while True:
        try:
            guess: int = int(input("Guess the secret number: "))
            if guess == number:
                break
            elif guess < number:
                print("Too low\n")
            else:
                print("Too high\n")
        except ValueError:
            print("Invalid input! Please enter an valid Integer!\n")

    print("Correct Answer!")


if __name__ == "__main__":
    guessing_game()
