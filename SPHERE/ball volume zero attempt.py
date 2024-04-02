import math

def sphere_volume(radius):
    """Calculate the volume of a sphere."""
    volume = (4/3) * math.pi * radius**3
    return volume

while True:
    user_input_radius = input("Enter the radius of the sphere (or type 'quit' to exit): ")

    if user_input_radius.lower() == 'quit':
        print("Exiting the program.")
        break

    try:
        # Validate user input
        radius = float(user_input_radius)
        if radius < 0:
            print("Please enter a non-negative value for the radius.")
        else:
            # Calculate and print the volume
            volume = sphere_volume(radius)
            print(f"The volume of the sphere with radius {radius} is: {volume}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the radius.")