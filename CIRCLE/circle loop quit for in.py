import turtle
import math

def draw_star(size):
    count = 0
    while count < 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1

def draw_circle_with_star(radius, star_size, pi_value):
    if pi_value == '3.14':
        turtle.circle(radius)
    elif pi_value == '22/7':
        turtle.circle(radius, math.radians(360))  # Approximating a full circle using 360 degrees
    else:
        print("Invalid choice for pi value.")
        return

    draw_star(star_size)

def quit_app(x, y):
    turtle.bye()

# Set the number of iterations
num_iterations = 3

for _ in range(num_iterations):
    # Get user input for circle radius, star size, and pi value
    try:
        user_input = input("Enter circle radius, star size, and pi value (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            break

        radius, star_size, pi_choice = map(str.strip, user_input.split())

        radius = float(radius)
        star_size = float(star_size)

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    else:
        # Set up Turtle window
        turtle.speed(2)
        turtle.bgcolor("white")

        # Draw a circle with a star inside based on user input
        draw_circle_with_star(radius, star_size, pi_choice)

        # Create a Quit button
        quit_button = turtle.Turtle()
        quit_button.hideturtle()
        quit_button.penup()
        quit_button.goto(-150, -150)
        quit_button.write("Quit", font=("Arial", 16, "normal"))
        quit_button.onclick(quit_app)

        # Keep the window open until closed by the user
        turtle.mainloop()
        turtle.reset()  # Reset turtle for the next iteration