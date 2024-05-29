import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)

        code.append(color)

    return code


def guess_code():
    while True:
        guess = input("Guess: ").upper().strip()
        print(guess)

        if guess.count(" ") != CODE_LENGTH - 1:
            print("You must add space between each code. Try again")
            continue

        else:
            guess = guess.split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors!")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again!")
                break

        else:
            break

    return guess
