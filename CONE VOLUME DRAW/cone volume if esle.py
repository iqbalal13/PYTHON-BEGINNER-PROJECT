import turtle

def draw_cone(height, radius):
    # Set up the Turtle screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a Turtle object
    cone_turtle = turtle.Turtle()
    cone_turtle.speed(2)

    # Draw the cone
    cone_turtle.penup()
    cone_turtle.goto(0, -height/2)
    cone_turtle.pendown()
    cone_turtle.circle(radius, 180)
    cone_turtle.goto(0, -height/2)
    cone_turtle.pendown()
    cone_turtle.forward(height)

    # Wait for the user to close the window
    turtle.done()

def get_user_input():
    height_input = input("Enter the height of the cone: ")
    radius_input = input("Enter the radius of the cone: ")

    if height_input.replace(".", "", 1).isdigit() and radius_input.replace(".", "", 1).isdigit():
        height = float(height_input)
        radius = float(radius_input)
        return height, radius
    else:
        print("Invalid input. Please enter valid numeric values.")
        return get_user_input()

def main():
    # Get user input for cone dimensions
    height, radius = get_user_input()

    # Draw the cone
    draw_cone(height, radius)

if __name__ == "__main__":
    main()