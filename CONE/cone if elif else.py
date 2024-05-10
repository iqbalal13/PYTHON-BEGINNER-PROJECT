import math

def cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

# Get user input for radius
radius_input = input("Enter the radius of the cone: ")
if radius_input.replace('.', '', 1).isdigit():  # Check if the input is a valid float
    radius = float(radius_input)
else:
    print("Invalid input. Please enter a numeric value for the radius.")
    exit()

# Get user input for height
height_input = input("Enter the height of the cone: ")
if height_input.replace('.', '', 1).isdigit():  # Check if the input is a valid float
    height = float(height_input)
else:
    print("Invalid input. Please enter a numeric value for the height.")
    exit()

# Calculate the volume using the function
result = cone_volume(radius, height)

# Display the result
print(f"The volume of the cone with radius {radius} and height {height} is: {result}")