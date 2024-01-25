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

def quit_app():
    turtle.bye()

# Get user input for circle radius and star size
try:
    radius_input = input("Enter the radius of the circle: ")
    star_size_input = input("Enter the size of the star: ")

    radius = float(radius_input)
    star_size = float(star_size_input)

except ValueError:
    print("Invalid input. Please enter numeric values.")
else:
    # Set up Turtle window
    turtle.speed(2)
    turtle.bgcolor("white")

    # Draw a circle with a star inside based on user input
    draw_circle_with_star(radius, star_size)

    # Create a Quit button
    quit_button = turtle.Turtle()
    quit_button.hideturtle()
    quit_button.penup()
    quit_button.goto(-150, -150)
    quit_button.write("Quit", font=("Arial", 16, "normal"))
    quit_button.onclick(quit_app)

    # Keep the window open until closed by the user
    turtle.mainloop()