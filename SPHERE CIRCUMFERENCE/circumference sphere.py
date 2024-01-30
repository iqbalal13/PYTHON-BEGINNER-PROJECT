import math

def sphere_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

# Example usage:
radius = float(input("Enter the radius of the sphere: "))
result = sphere_circumference(radius)
print(f"The circumference of the sphere with radius {radius} is: {result}")