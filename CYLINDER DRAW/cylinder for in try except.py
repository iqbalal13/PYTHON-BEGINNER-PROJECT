import turtle
import math

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

def get_user_input():
    for _ in range(3):  # Allow three attempts for valid input
        try:
            radius_input = input("Enter the radius of the cylinder: ")
            height_input = input("Enter the height of the cylinder: ")

            radius = float(radius_input)
            height = float(height_input)

            return radius, height

        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

    # If three attempts are unsuccessful, return default values
    print("Exceeded maximum attempts. Using default values.")
    return 0, 0

def main():
    try:
        # Get user input for cylinder dimensions
        radius, height = get_user_input()

        # Draw the cylinder
        draw_cylinder(radius, height)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()