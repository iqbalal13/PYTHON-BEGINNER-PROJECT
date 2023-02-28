import turtle

# Create the screen
screen = turtle.Screen()
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(width=600, height=400)

# Create the left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-250, 0)

# Create the right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(250, 0)

# Create the ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Set the score to zero
left_score = 0
right_score = 0

# Create the score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 170)
score_display.write("Player 1: {}  Player 2: {}".format(left_score, right_score), align="center", font=("Courier", 16, "normal"))

# Move the left paddle up
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

# Move the left paddle down
def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

# Move the right paddle up
def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

# Move the right paddle down
def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# Keyboard bindings
screen.listen()
screen.onkeypress(left_paddle_up, "w")
screen.onkeypress(left_paddle_down, "s")
screen.onkeypress(right_paddle_up, "Up")
screen.onkeypress(right_paddle_down, "Down")

# Main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for top and bottom borders
    if ball.ycor() > 190:
        ball.sety(190)
        ball.dy *= -1

    if ball.ycor() < -190:
        ball.sety(-190)
        ball.dy *= -1

    # Check for left and right borders
    if ball.xcor() > 290:
        ball.goto(0, 0)
        ball.dy *= -1
        left_score += 1
        score_display.clear()
        score_display.write("Player 1: {}  Player 2: {}".format(left_score, right_score), align="center", font=("Courier", 16, "normal"))

    if ball.xcor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1
        right_score += 1
        score_display.clear()
        score_display.write("Player 1: {}  Player 2: {}".format(left_score, right_score), align="center", font=("Courier", 16, "normal"))