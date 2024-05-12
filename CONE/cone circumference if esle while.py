import math

def cone_circumference(radius, slant_height):
    if radius <= 0 or slant_height <= 0:
        print("Invalid input. Radius and slant height must be positive values.")
        return None
    
    # Calculate the circumference using the formula
    circumference = 2 * math.pi * radius + slant_height
    return circumference

while True:
    try:
        # Example usage within a loop
        radius = float(input("Enter the radius of the cone: "))
        slant_height = float(input("Enter the slant height of the cone: "))

        result = cone_circumference(radius, slant_height)

        if result is not None:
            print(f"The circumference of the cone is: {result}")
            break  # Exit the loop if valid input and calculation are successful
    except ValueError:
        print("Invalid input. Please enter valid numerical values for radius and slant height.")