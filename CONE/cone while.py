import math

def cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

# Initialize variables
radius = None
height = None

# Get user input for radius with error handling using a while loop
while radius is None:
    radius_input = input("Enter the radius of the cone: ")
    if radius_input.replace('.', '', 1).isdigit():
        radius = float(radius_input)
    else:
        print("Invalid input. Please enter a numeric value for the radius.")

# Get user input for height with error handling using a while loop
while height is None:
    height_input = input("Enter the height of the cone: ")
    if height_input.replace('.', '', 1).isdigit():
        height = float(height_input)
    else:
        print("Invalid input. Please enter a numeric value for the height.")

# Calculate the volume using the function
result = cone_volume(radius, height)

# Display the result
print(f"The volume of the cone with radius {radius} and height {height} is: {result}")