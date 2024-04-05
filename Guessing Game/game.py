import random

global min_number, max_number

print("Welcome to the Guess Game!")
while True:
    try:
        max_number = int(input("Enter the max number: "))
        min_number = 1
        if max_number > 1:
            break
        else:
            print("Pick a number greater than 1.")
            continue
    except ValueError:
        print("Invalid input. Try again.")
        continue

random_number = random.randint(min_number, max_number)
guesses = 0

while True:
    try:
        guess = int(input(f"Guess a number between 1 and {max_number}: "))
        if 1 <= guess <= max_number:
            if guess < random_number:
                print("Too Low!")
                guesses += 1
            elif guess > random_number:
                print("Too High!")
                guesses += 1
            else:
                print("You guessed it right!")
                print(f"The number was {random_number} with {guesses} guesses.")
                break
        else:
            print("Number is out of range!")
    except ValueError:
        print("Invalid input!")
