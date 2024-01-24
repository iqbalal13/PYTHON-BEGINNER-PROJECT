import turtle

def draw_star(size):
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)

def draw_circle_with_star(radius, star_size):
    turtle.circle(radius)
    draw_star(star_size)

# Set up Turtle window
turtle.speed(2)  # Set the drawing speed (1 is slowest, 10 is fastest)
turtle.bgcolor("white")  # Set the background color

# Draw a circle with a star inside
draw_circle_with_star(100, 50)

# Keep the window open until closed by the user
turtle.mainloop()