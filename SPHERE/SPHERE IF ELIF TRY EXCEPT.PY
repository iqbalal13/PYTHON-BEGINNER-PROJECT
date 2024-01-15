import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

# Input validation with try-except
try:
    radius = float(input("Enter the radius of the sphere: "))
    if radius > 0:
        volume = sphere_volume(radius)
        print(f"The volume of the sphere with radius {radius} is: {volume}")
    elif radius == 0:
        print("The radius should be a positive number.")
    else:
        print("Invalid input. Please enter a positive number for the radius.")
except ValueError:
    print("Invalid input. Please enter a valid number for the radius.")