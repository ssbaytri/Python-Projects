import turtle

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
    screen.mainloop()


racers = get_number_of_players()
init_turtle()
