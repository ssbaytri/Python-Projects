import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll

while True:
    players = input("Enter the number of players (2 -> 4): ")
    if players.isdigit():
        players = int(players)
        if players >= 2 and players <= 4:
            break
        else:
            print("Please enter a number between 2 and 4.")
    else:
        print("Invalid Input, try again.")

max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:
    for player_idx in range(players):
        print("\nPlayer", + player_idx + 1 )