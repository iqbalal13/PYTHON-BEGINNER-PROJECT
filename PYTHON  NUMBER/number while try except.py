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

while True:
    # Take user input for the number to draw
    user_input = input("Enter a number (1-3) to draw, or 'q' to quit: ")

    if user_input.lower() == 'q':
        break  # Exit the loop if the user enters 'q'

    try:
        number_to_draw = int(user_input)
        if 1 <= number_to_draw <= 3:
            draw_number(number_to_draw)
        else:
            print("Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")