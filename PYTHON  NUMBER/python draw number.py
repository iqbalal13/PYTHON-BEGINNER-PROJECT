import turtle

def draw_number(number):
    # Set up the turtle
    screen = turtle.Screen()
    screen.title("Draw Number")

    pen = turtle.Turtle()
    pen.speed(2)  # Set the drawing speed

    # Define the drawing instructions for each number
    if number == 1:
        pen.forward(100)
        pen.backward(50)
        pen.right(90)
        pen.forward(100)
    elif number == 2:
        pen.circle(50, -180)
        pen.left(90)
        pen.forward(100)
        pen.right(90)
        pen.forward(100)
    elif number == 3:
        pen.circle(50, -180)
        pen.right(180)
        pen.forward(100)
        pen.left(90)
        pen.forward(100)
    # Add more cases for other numbers as needed

    # Close the drawing window on click
    screen.exitonclick()

# Example: Draw the number 2
draw_number(2)