import turtle

def draw_star(size):
    # Draw a star inside the circle
    i = 0
    while i < 5:
        turtle.forward(size)
        turtle.right(144)
        i += 1

def draw_circle_with_star(radius):
    # Set up the turtle
    turtle.speed(2)
    
    # Draw the circle
    turtle.circle(radius)

    # Draw the star inside the circle
    draw_star(radius / 2)

    # Close the drawing window on click
    turtle.exitonclick()

# Specify the radius of the circle
circle_radius = 100

# Draw the circle with a star inside
draw_circle_with_star(circle_radius)