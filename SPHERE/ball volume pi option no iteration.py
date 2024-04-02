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
        # Validate user input for radius
        radius = float(user_input_radius)
        if radius < 0:
            print("Please enter a non-negative value for the radius.")
            continue

        # Ask the user to choose the value of pi
        pi_option = input("Choose the value of pi (3.14 or 22/7): ").lower()

        if pi_option not in ['3.14', '22/7']:
            print("Invalid pi option. Please choose either '3.14' or '22/7'.")
            continue

        # Calculate and print the volume using the chosen pi
        pi_value = float(pi_option)
        volume = sphere_volume(radius)
        print(f"The volume of the sphere with radius {radius} and pi {pi_option} is: {volume}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the radius.")