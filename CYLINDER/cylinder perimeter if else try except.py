import math

def cylinder_circumference(radius):
    return 2 * math.pi * radius

# Example usage with if-else statement:
try:
    radius = float(input("Enter the radius of the cylinder: "))
    
    if radius > 0:
        circumference = cylinder_circumference(radius)
        print(f"The circumference of the base of the cylinder is: {circumference}")
    else:
        print("Please enter a positive value for the radius.")
except ValueError:
    print("Invalid input. Please enter a valid number.")