import turtle

def draw_star(size):
    # Draw a star inside the circle
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

def draw_circle_with_star(radius):
    # Set up the turtle
    turtle.speed(2)
    turtle.circle(radius)  # Draw the circle
    draw_star(radius / 2)  # Draw the star inside the circle

    # Close the drawing window on click
    turtle.exitonclick()

# Specify the radius of the circle
circle_radius = 100

# Draw the circle with a star inside
draw_circle_with_star(circle_radius)