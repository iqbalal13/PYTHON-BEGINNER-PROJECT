import math

def sphere_circumference(radius):
    if radius >= 0:
        circumference = 2 * math.pi * radius
        return circumference
    else:
        return "Error: Radius should be a non-negative value."

# Example usage:
try:
    radius = float(input("Enter the radius of the sphere: "))
    result = sphere_circumference(radius)
    print(f"The circumference of the sphere with radius {radius} is: {result}")
except ValueError:
    print("Error: Please enter a valid numeric value for the radius.")