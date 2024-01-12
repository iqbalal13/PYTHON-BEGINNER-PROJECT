

def cylinder_volume(radius, height):
    """Calculate the volume of a cylinder."""
    volume = math.pi * radius**2 * height
    return volume

# Get user input for the radius and height
try:
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))

    if radius < 0 or height < 0:
        print("Please enter non-negative values for radius and height.")
    else:
        # Calculate and print the volume
        volume = cylinder_volume(radius, height)
        print(f"The volume of the cylinder is: {volume}")
except ValueError:
    print("Invalid input. Please enter valid numeric values for the radius and height.")