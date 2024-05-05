import turtle
import time
import random

WIDTH, HEIGHT = 500, 500

COLORS = ["red", "green", "blue", "orange", "yellow", "black", "purple", "pink", "brown", "cyan"]

def get_number_of_players():
    racers = 0
    while True:
        racers = input("Enter the racers number (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please entrer a number!")
            continue
        
        if 2 <= racers <= 10:
            return racers
        else:
            print("Invalid Number!")


def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            racer.speed(1)
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()

            if y >= (HEIGHT // 2 - 20):
                return colors[turtles.index(racer)]



def create_turtles(colors):
    turtles = []
    spacingX = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.speed(2)
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH // 2 + (i + 1) * spacingX, -HEIGHT // 2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles



def init_turtle():
    screen = turtle.Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor("#d1d1d1")
    screen.title("Turtle Racing")


racers = get_number_of_players()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
print(f"The winner is the {winner} turtle")
time.sleep(5)
