import turtle
import math

def draw_cylinder(radius, height):
    # Set up the Turtle screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a Turtle object
    cylinder_turtle = turtle.Turtle()
    cylinder_turtle.speed(2)

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

def get_user_input():
    radius_input = input("Enter the radius of the cylinder: ")
    height_input = input("Enter the height of the cylinder: ")

    if radius_input.replace(".", "", 1).isdigit() and height_input.replace(".", "", 1).isdigit():
        radius = float(radius_input)
        height = float(height_input)
        return radius, height
    else:
        print("Invalid input. Please enter valid numeric values.")
        return get_user_input()

def main():
    # Get user input for cylinder dimensions
    radius, height = get_user_input()

    # Draw the cylinder
    draw_cylinder(radius, height)

if __name__ == "__main__":
    main()