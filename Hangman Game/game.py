# Hangman Game

import random

words = ("computer", "space", "energy", "pickaxe", "science", "delivery")

# Hangman stages dictionary
hangman_stages = {
    0: """
       ------
       |    |
       |
       |
       |
       |
       |
    --------""",
    1: """
       ------
       |    |
       |    O
       |
       |
       |
       |
    --------""",
    2: """
       ------
       |    |
       |    O
       |    |
       |
       |
       |
    --------""",
    3: """
       ------
       |    |
       |    O
       |   /|
       |
       |
       |
    --------""",
    4: """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
       |
    --------""",
    5: """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
       |
    --------""",
    6: """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
       |
    --------""",
}


def display_man(wrong_guesses):
    pass


def display_hint(hint):
    pass


def display_answer(answer):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
