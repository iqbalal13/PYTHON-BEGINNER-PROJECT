import math

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

# Get user input for the radius
try:
    radius = float(input("Enter the radius of the circle: "))
except ValueError:
    print("Invalid input. Please enter a numeric value for the radius.")
else:
    # Calculate and display the circumference
    circumference = calculate_circumference(radius)
    print(f"The circumference of the circle with radius {radius} is {circumference:.2f}")