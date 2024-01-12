import math

def cylinder_volume(radius, height, pi_value):
    """Calculate the volume of a cylinder."""
    volume = pi_value * radius**2 * height
    return volume

# Loop for user input
max_attempts = 3
for _ in range(max_attempts):
    try:
        radius_input = input("Enter the radius of the cylinder: ")
        height_input = input("Enter the height of the cylinder: ")

        # Get user input for the choice of pi value
        print("Choose the value of pi:")
        print("1. 3.14")
        print("2. 22/7")
        pi_choice = input("Enter your choice (1 or 2): ")

        # Validate user input
        if (
            radius_input.replace('.', '', 1).isdigit() and
            height_input.replace('.', '', 1).isdigit() and
            pi_choice.isdigit()
        ):
            radius = float(radius_input)
            height = float(height_input)

            if radius < 0 or height < 0:
                print("Please enter non-negative values for radius and height.")
            else:
                # Choose pi value based on user's choice
                if pi_choice == "1":
                    pi_value = 3.14
                elif pi_choice == "2":
                    pi_value = 22/7
                else:
                    print("Invalid choice for pi value. Using default value 3.14.")
                    pi_value = 3.14

                # Calculate and print the volume
                volume = cylinder_volume(radius, height, pi_value)
                print(f"The volume of the cylinder is: {volume}")
                break  # Exit the loop if input is valid
        else:
            print("Invalid input. Please enter valid numeric values for the radius and height.")
    except ValueError:
        print("Invalid input. Please enter valid numeric values for the radius and height.")
else:
    print(f"You've reached the maximum number of attempts ({max_attempts}). Exiting.")