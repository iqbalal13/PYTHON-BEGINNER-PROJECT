import math

def cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

# Example usage:
radius = 3.0
height = 5.0
result = cone_volume(radius, height)

print(f"The volume of the cone with radius {radius} and height {height} is: {result}")