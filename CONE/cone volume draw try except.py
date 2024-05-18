import turtle

def draw_cone(height, radius):
    # Set up the Turtle screen
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Create a Turtle object
    cone_turtle = turtle.Turtle()
    cone_turtle.speed(2)

    try:
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
    
    except turtle.Terminator:
        # Handle if the user closes the window prematurely
        print("Window closed. Program terminated.")

def get_user_input():
    try:
        height = float(input("Enter the height of the cone: "))
        radius = float(input("Enter the radius of the cone: "))
        return height, radius
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_input()

def main():
    try:
        # Get user input for cone dimensions
        height, radius = get_user_input()

        # Draw the cone
        draw_cone(height, radius)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()