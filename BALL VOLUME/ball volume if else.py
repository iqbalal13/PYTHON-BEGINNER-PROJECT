import math

def sphere_volume(radius):
    """Calculate the volume of a sphere."""
    volume = (4/3) * math.pi * radius**3
    return volume

# Get user input for the radius
user_input = input("Enter the radius of the sphere: ")

# Validate user input
try:
    radius = float(user_input)
    if radius < 0:
        print("Please enter a non-negative value for the radius.")
    else:
        # Calculate and print the volume
        volume = sphere_volume(radius)
        print(f"The volume of the sphere with radius {radius} is: {volume}")
except ValueError:
    print("Invalid input. Please enter a valid numeric value for the radius.")