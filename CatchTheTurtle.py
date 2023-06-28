import turtle
import random

# Game Board
game_board = turtle.Screen()
game_board.bgcolor("#d3ffce")
game_board.title("Catch The Turtle")

# Our Turtle
game_turtle = turtle.Turtle()
game_turtle.color('#453534')
game_turtle.shape("turtle")
game_turtle.shapesize(2, 2)
game_turtle.penup()

# Score Board
turtle.tracer(0)
score = 0
screen_turtle = turtle.Turtle()
screen_turtle.hideturtle()
screen_turtle.pencolor('red')
screen_turtle.penup()
top_height = game_board.window_height() / 2
y_axis1 = top_height * 0.88
screen_turtle.goto(0, y_axis1)
screen_turtle.write(arg="Score = {}".format(score), move=False, align='center', font=('Monaco', 30, 'normal'))


# Countdown Board
countdown = turtle.Turtle()
countdown.hideturtle()
countdown.pencolor('blue')
countdown.penup()
top_height = game_board.window_height() / 2
y_axis2 = top_height * 0.78
countdown.goto(0, y_axis2)
countdown.write('Time = 0', move=False, align='center', font=('Monaco', 30, 'normal'))
turtle.tracer(1)

game_over = False


# Setting random position, blinking time and increase score
def random_pos():
    if not game_over:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        game_turtle.hideturtle()
        game_turtle.goto(x, y)
        game_turtle.showturtle()

    def increase_score(a, b):
        global score
        score += 1
        screen_turtle.clear()
        screen_turtle.write(arg="Score = {}".format(score), move=False, align='center', font=('Monaco', 30, 'normal'))
    game_turtle.onclick(increase_score)
    game_board.ontimer(random_pos, 700)


random_pos()

# Countdown and ending the game


def oclock(time):
    global game_over
    if time > 0:
        countdown.clear()
        countdown.write('Time = {}'.format(time), move=False, align='center', font=('Monaco', 30, 'normal'))
        game_board.ontimer(lambda: oclock(time - 1), 1000)

    else:
        game_over = True
        countdown.clear()
        game_turtle.hideturtle()
        countdown.write('Game Over!!!', move=False, align='center', font=('Monaco', 30, 'normal'))


oclock(30)

turtle.mainloop()
