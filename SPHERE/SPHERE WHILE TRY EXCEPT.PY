import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

while True:
    try:
        radius = float(input("Enter the radius of the sphere: "))
        if radius <= 0:
            raise ValueError("The radius should be a positive number.")
        
        volume = sphere_volume(radius)
        print(f"The volume of the sphere with radius {radius} is: {volume}")
        break  # Break out of the loop if a valid radius is entered
    except ValueError as e:
        print(f"Invalid input: {e}")