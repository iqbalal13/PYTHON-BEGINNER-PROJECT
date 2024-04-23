import math

def cylinder_circumference(radius):
    return 2 * math.pi * radius

# Example usage with if-else statement for input validation:
radius_input = input("Enter the radius of the cylinder: ")

if radius_input.replace('.', '', 1).lstrip('-').isdigit():  # Check if input is a positive or negative number
    radius = float(radius_input)

    if radius > 0:
        circumference = cylinder_circumference(radius)
        print(f"The circumference of the base of the cylinder is: {circumference}")
    else:
        print("Please enter a positive value for the radius.")
else:
    print("Invalid input. Please enter a valid number.")