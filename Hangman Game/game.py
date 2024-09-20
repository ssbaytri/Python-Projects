# Hangman Game

import random

words = ("computer", "space", "energy", "pickaxe", "science", "delivery", "work", "gem")

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
    print(hangman_stages[wrong_guesses])


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    running = True

    while running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input!")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed!")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You Won!")
            running = False
        elif wrong_guesses >= len(hangman_stages) - 1:
            display_man(wrong_guesses)
            print("You Lost!, The answer was: ")
            display_answer(answer)
            running = False



if __name__ == "__main__":
    main()
