import turtle
import math
import sys

def draw_cylinder(radius, height):
    # Set up the Turtle screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a Turtle object
    cylinder_turtle = turtle.Turtle()
    cylinder_turtle.speed(2)

    try:
        # Draw the cylinder
        # Draw the top circle
        cylinder_turtle.penup()
        cylinder_turtle.goto(0, height/2)
        cylinder_turtle.pendown()
        cylinder_turtle.circle(radius)

        # Draw the bottom circle
        cylinder_turtle.penup()
        cylinder_turtle.goto(0, -height/2)
        cylinder_turtle.pendown()
        cylinder_turtle.circle(radius)

        # Connect the top and bottom circles to complete the cylinder
        cylinder_turtle.penup()
        cylinder_turtle.goto(0, height/2)
        cylinder_turtle.pendown()
        cylinder_turtle.setheading(-90)
        cylinder_turtle.forward(height)
        
        # Wait for the user to close the window
        turtle.done()

    except turtle.Terminator:
        # Handle if the user closes the window prematurely
        print("Window closed. Program terminated.")
        sys.exit()

def get_user_input():
    for _ in range(sys.maxsize):  # Infinite loop until 'exit' is entered
        user_input = input("Enter the radius and height of the cylinder (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting program.")
            sys.exit()

        try:
            radius, height = map(float, user_input.split())
            return radius, height

        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

def main():
    try:
        for _ in range(sys.maxsize):  # Infinite loop until 'exit' is entered
            # Get user input for cylinder dimensions
            radius, height = get_user_input()

            # Draw the cylinder
            draw_cylinder(radius, height)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()