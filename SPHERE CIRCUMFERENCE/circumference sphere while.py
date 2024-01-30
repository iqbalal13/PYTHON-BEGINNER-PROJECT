import math

def sphere_circumference(radius):
    if radius >= 0:
        circumference = 2 * math.pi * radius
        return circumference
    else:
        return "Error: Radius should be a non-negative value."

# Example usage with while loop:
while True:
    try:
        radius = float(input("Enter the radius of the sphere: "))
        result = sphere_circumference(radius)
        
        if isinstance(result, str):
            print(result)
        else:
            print(f"The circumference of the sphere with radius {radius} is: {result}")
            
        break  # Break out of the loop if input is valid
    except ValueError:
        print("Error: Please enter a valid numeric value for the radius.")