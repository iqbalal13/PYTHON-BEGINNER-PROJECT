import math

def cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

# Get user input for radius and height
radius = float(input("Enter the radius of the cone: "))
height = float(input("Enter the height of the cone: "))

# Calculate the volume using the function
result = cone_volume(radius, height)

# Display the result
print(f"The volume of the cone with radius {radius} and height {height} is: {result}")