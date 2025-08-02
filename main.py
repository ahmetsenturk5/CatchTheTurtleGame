import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Catch the Turtle")

WELCOME_FONT = ("Comic Sans MS", 28, "bold")
GAME_FONT = ("Arial", 24, "normal")
score = 0
game_over = False
game_duration = 30

turtle_list = []

score_turtle = turtle.Turtle()
countdown_turtle = turtle.Turtle()
welcome_turtle = turtle.Turtle()

x_cordinates = [-20, -10, 0, 10, 20]
y_cordinates = [-10, 0, 10, 20]
grid_size = 10


def show_welcome_message():
    welcome_turtle.clear()
    welcome_turtle.penup()
    welcome_turtle.speed(0)
    welcome_turtle.shape("blank")
    welcome_turtle.color("green")
    welcome_turtle.goto(0, 0)
    welcome_turtle.hideturtle()
    welcome_turtle.write("Welcome Catch the Turtle Game!", align="center", font=WELCOME_FONT)


    screen.ontimer(ask_game_duration, 5000)


def ask_game_duration():
    global game_duration
    welcome_turtle.clear()

    answer = screen.textinput("Choose Duration", "How many seconds do you want the game to last? (10–60)")

    try:
        val = int(answer)
        if 10 <= val <= 60:
            game_duration = val
        else:
            print("Invalid number. Please enter a value between 10 and 60.")
    except:
        print("Invalid input. Default time will be used.")

    start_game_up()



def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.9
    score_turtle.setposition(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=GAME_FONT)


def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x, y):
        global score
        if not game_over:
            score += 1
            score_turtle.clear()
            score_turtle.write(arg="Score: {}".format(score), move=False, align="center", font=GAME_FONT)

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t)


def setup_turtle():
    for x in x_cordinates:
        for y in y_cordinates:
            make_turtle(x, y)


def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


def show_turtles_randomly():
    if not game_over:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtles_randomly, 500)


def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = screen.window_height() / 2
    y = top_height * 0.8
    countdown_turtle.setposition(0, y - 10)
    countdown_turtle.clear()
    if time > 0:
        countdown_turtle.write(arg="Time: {}".format(time), move=False, align="center", font=GAME_FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        hide_turtles()
        countdown_turtle.clear()
        countdown_turtle.write(arg="Game Over", move=False, align="center", font=GAME_FONT)


def start_game_up():
    turtle.tracer(0)
    setup_score_turtle()
    setup_turtle()
    hide_turtles()
    show_turtles_randomly()
    countdown(game_duration)
    turtle.tracer(1)


show_welcome_message()
turtle.mainloop()
