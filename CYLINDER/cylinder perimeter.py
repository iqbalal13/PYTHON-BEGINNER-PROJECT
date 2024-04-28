import math

def cylinder_circumference(radius):
    return 2 * math.pi * radius

# Example usage:
radius = float(input("Enter the radius of the cylinder: "))
circumference = cylinder_circumference(radius)

print(f"The circumference of the base of the cylinder is: {circumference}")