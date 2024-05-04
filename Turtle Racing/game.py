import turtle
import time

WIDTH, HEIGHT = 500, 500

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


def init_turtle():
    screen = turtle.Screen()
    screen.setup(width=WIDTH, height=HEIGHT)
    screen.bgcolor("#d1d1d1")
    screen.title("Turtle Racing")


racers = get_number_of_players()
init_turtle()

racer = turtle.Turtle(shape="turtle")
racer.speed(1)
racer.color("red")
racer.penup()
racer.left(90)
racer.forward(100)
racer.right(90)
racer.forward(100)
time.sleep(5)
