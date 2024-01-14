
def cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

# Get user input for radius with error handling using try-except
try:
    radius_input = input("Enter the radius of the cone: ")
    radius = float(radius_input)
except ValueError:
    print("Invalid input. Please enter a numeric value for the radius.")
    exit()

# Get user input for height with error handling using try-except
try:
    height_input = input("Enter the height of the cone: ")
    height = float(height_input)
except ValueError:
    print("Invalid input. Please enter a numeric value for the height.")
    exit()

# Calculate the volume using the function
result = cone_volume(radius, height)

# Display the result
print(f"The volume of the cone with radius {radius} and height {height} is: {result}")


import math

def cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

# Get user input for radius with error handling using try-except
try:
    radius_input = input("Enter the radius of the cone: ")
    radius = float(radius_input)

    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
except ValueError as ve:
    print(f"Invalid input for radius: {ve}")
    exit()

# Get user input for height with error handling using try-except
try:
    height_input = input("Enter the height of the cone: ")
    height = float(height_input)

    if height <= 0:
        raise ValueError("Height must be a positive number.")
except ValueError as ve:
    print(f"Invalid input for height: {ve}")
    exit()

# Calculate the volume using the function
result = cone_volume(radius, height)

# Display the result
print(f"The volume of the cone with radius {radius} and height {height} is: {result}")