import math

def cone_circumference(radius, slant_height):
    # Calculate the circumference using the formula
    circumference = 2 * math.pi * radius + slant_height
    return circumference

# Example usage:
radius = float(input("Enter the radius of the cone: "))
slant_height = float(input("Enter the slant height of the cone: "))

result = cone_circumference(radius, slant_height)
print(f"The circumference of the cone is: {result}")