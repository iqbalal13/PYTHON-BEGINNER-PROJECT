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

def main():
    try:
        # Get user input for cylinder dimensions
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))

        # Draw the cylinder
        draw_cylinder(radius, height)

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")

if __name__ == "__main__":
    main()