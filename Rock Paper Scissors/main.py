import random

print("Welcome to Rock Paper Scissors game!")

game_options = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

while True:
    user_input = input("Enter your choice: Rock, Paper, Scissors or q to quit: ").lower()
    if user_input == "q":
        break
    elif user_input in game_options:
        random_choice = random.randint(0, len(game_options) - 1)
        computer_choice = game_options[random_choice]
        print("Computer chose: " + computer_choice + ".")

        if user_input == "rock" and computer_choice == "scissors":
            user_wins += 1
            print("You won!")

        elif user_input== "paper" and computer_choice == "rock":
            user_wins += 1
            print("You won!")

        elif user_input == "scissors" and computer_choice == "paper":
            user_wins += 1
            print("You won!")

        elif user_input == computer_choice:
            print("draw!")

        else:
            print("You Lost!")
            computer_wins += 1

    else:
        print("Invalid Input!")

print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")