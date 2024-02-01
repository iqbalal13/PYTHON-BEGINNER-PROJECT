import math
import itertools

def sphere_circumference(radius):
    if radius >= 0:
        circumference = 2 * math.pi * radius
        return circumference
    else:
        return "Error: Radius should be a non-negative value."

# Example usage with try-except and an endless while loop with a quit option:
attempt_counter = itertools.count(1)  # Create an iterator for the attempt counter

while True:
    attempt = next(attempt_counter)
    radius_input = input(f"Attempt {attempt}: Enter the radius of the sphere (or type 'quit' to exit): ")

    if radius_input.lower() == 'quit' or radius_input.lower() == 'q':
        print("Exiting the program.")
        break  # Break out of the loop if the user wants to quit

    try:
        radius = float(radius_input)
    except ValueError:
        print("Error: Please enter a valid numeric value for the radius.")
        continue  # Skip the rest of the loop and start the next iteration

    result = sphere_circumference(radius)

    if isinstance(result, str):
        print(result)
    else:
        print(f"The circumference of the sphere with radius {radius} is: {result}")
        break  # Break out of the loop if input is valid