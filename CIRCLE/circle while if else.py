import turtle

def draw_star(size):
    count = 0
    while count < 5:
        turtle.forward(size)
        turtle.right(144)
        count += 1

def draw_circle_with_star(radius, star_size):
    turtle.circle(radius)
    draw_star(star_size)

# Get user input for circle radius and star size
radius_input = input("Enter the radius of the circle: ")
star_size_input = input("Enter the size of the star: ")

if radius_input.replace('.', '', 1).isdigit() and star_size_input.replace('.', '', 1).isdigit():
    radius = float(radius_input)
    star_size = float(star_size_input)
    # Set up Turtle window
    turtle.speed(2)
    turtle.bgcolor("white")

    # Draw a circle with a star inside based on user input
    draw_circle_with_star(radius, star_size)

    # Keep the window open until closed by the user
    turtle.mainloop()
else:
    print("Invalid input. Please enter numeric values.")