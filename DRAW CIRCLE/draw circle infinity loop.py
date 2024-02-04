import turtle
from itertools import count

def draw_star(size):
    # Draw a star inside the circle
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

def draw_circle_with_star(radius):
    # Set up the turtle
    turtle.speed(2)
    
    # Draw the circle
    turtle.circle(radius)

    # Draw the star inside the circle
    draw_star(radius / 2)

# Infinite loop to draw circles with stars
for counter in count():
    # Specify the radius of the circle
    circle_radius = int(input("Enter the radius for the next circle (enter 0 to exit): "))
    
    # Exit the loop if the user enters 0
    if circle_radius == 0:
        break
    
    # Draw the circle with a star inside if the radius is greater than 0
    if circle_radius > 0:
        draw_circle_with_star(circle_radius)
    else:
        print("Invalid radius. Please enter a positive value.")

# Close the drawing window on click
turtle.exitonclick()