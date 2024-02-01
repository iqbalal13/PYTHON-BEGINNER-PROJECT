import math
import itertools

def sphere_circumference(radius):
    if radius >= 0:
        circumference = 2 * math.pi * radius
        return circumference
    else:
        return "Error: Radius should be a non-negative value."

# Example usage without try-except and with an endless for loop with a quit option:
attempt_counter = itertools.count(1)  # Create an iterator for the attempt counter

for attempt in attempt_counter:
    radius_input = input(f"Attempt {attempt}: Enter the radius of the sphere (or type 'quit' to exit): ")

    if radius_input.lower() == 'quit' or radius_input.lower() == 'q':
        print("Exiting the program.")
        break  # Break out of the loop if the user wants to quit

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