import random

dice_faces = {
    1: (
        "┌─────────┐\n"
        "│         │\n"
        "│    ●    │\n"
        "│         │\n"
        "└─────────┘"
    ),
    2: (
        "┌─────────┐\n"
        "│  ●      │\n"
        "│         │\n"
        "│      ●  │\n"
        "└─────────┘"
    ),
    3: (
        "┌─────────┐\n"
        "│  ●      │\n"
        "│    ●    │\n"
        "│      ●  │\n"
        "└─────────┘"
    ),
    4: (
        "┌─────────┐\n"
        "│  ●   ●  │\n"
        "│         │\n"
        "│  ●   ●  │\n"
        "└─────────┘"
    ),
    5: (
        "┌─────────┐\n"
        "│  ●   ●  │\n"
        "│    ●    │\n"
        "│  ●   ●  │\n"
        "└─────────┘"
    ),
    6: (
        "┌─────────┐\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "│  ●   ●  │\n"
        "└─────────┘"
    )
}

dices = []
total = 0
num_of_dice = int(input("How many dice?: "))

for dice in range(num_of_dice):
    dices.append(random.randint(1, 6))

for dice in dices:
    print(dice_faces.get(dice))

for dice in dices:
    total += dice

print(f"Your total is: {total}")
