#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program lets the user guess a number between 1-10
#    with a randomized integer and tells them if they are correct or not
#       as well as loops until they get the answer


import random


def main():
    # this function lets the user pick a number between 1-10
    #   and randomizes said number as well as loops until they get the answer

    # input
    loop = 0
    guess_int = 1

    try:
        while loop < guess_int:

            guess = input("\nGuess an integer between 1-10: ")
            guess_int = int(guess)

            randomized_number = random.randint(1, 10)  # a number between 1-10

            # process & output
            if guess_int == randomized_number:
                print("\nYou are correct, the answer was {0}."
                      .format(randomized_number))
                break

            else:
                print("\nYou are not correct, the answer was {0}, try again."
                      .format(randomized_number))

    except Exception:
        print("\nYou have not entered an integer!")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
