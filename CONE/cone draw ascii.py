import turtle

# Function to draw a cone
def draw_cone(radius, height):
    turtle.speed(1)  # Set the drawing speed

    # Draw the base of the cone
    turtle.circle(radius)

    # Move the turtle to the top of the cone
    turtle.penup()
    turtle.goto(0, height)
    turtle.pendown()

    # Draw the lines connecting the top to the base
    turtle.goto(radius, 0)
    turtle.goto(-radius, 0)
    turtle.goto(0, height)

    turtle.done()

# Set the radius and height of the cone
cone_radius = 50
cone_height = 100

# Call the function to draw the cone
draw_cone(cone_radius, cone_height)