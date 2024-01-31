import math

def sphere_circumference(radius):
    if radius >= 0:
        circumference = 2 * math.pi * radius
        return circumference
    else:
        return "Error: Radius should be a non-negative value."

# Example usage without try-except and with an endless while loop:
max_attempts = 3  # Maximum number of attempts
attempt = 1  # Initialize attempt counter

while True:
    radius_input = input(f"Attempt {attempt}: Enter the radius of the sphere: ")

    if radius_input.replace('.', '', 1).isdigit():  # Check if the input is a valid float
        radius = float(radius_input)
        result = sphere_circumference(radius)

        if isinstance(result, str):
            print(result)
        else:
            print(f"The circumference of the sphere with radius {radius} is: {result}")
            break  # Break out of the loop if input is valid
    else:
        print("Error: Please enter a valid numeric value for the radius.")

    attempt += 1  # Increment the attempt counter

    if attempt > max_attempts:
        print(f"Maximum number of attempts ({max_attempts}) reached. Exiting.")
        break  # Break out of the loop if max_attempts are reached