import math

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

while True:
    # Get user input for the radius
    radius_input = input("Enter the radius of the circle (or 'quit' to exit): ")

    if radius_input.lower() == 'quit':
        break

    if radius_input.replace('.', '', 1).isdigit():
        radius = float(radius_input)
        # Calculate and display the circumference
        circumference = calculate_circumference(radius)
        print(f"The circumference of the circle with radius {radius} is {circumference:.2f}")
    else:
        print("Invalid input. Please enter a numeric value for the radius.")