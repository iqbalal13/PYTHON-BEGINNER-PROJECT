import math

def calculate_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference

# Set the number of iterations
num_iterations = 3
iteration_count = 0

while iteration_count < num_iterations:
    try:
        # Get user input for the radius
        radius_input = input("Enter the radius of the circle (or 'quit' to exit): ")

        if radius_input.lower() == 'quit':
            break

        radius = float(radius_input)
        # Calculate and display the circumference
        circumference = calculate_circumference(radius)
        print(f"The circumference of the circle with radius {radius} is {circumference:.2f}")

    except ValueError:
        print("Invalid input. Please enter a numeric value for the radius.")

    iteration_count += 1

# Additional iterations using for loop
for _ in range(iteration_count, num_iterations):
    print(f"Additional iteration {iteration_count + 1}")
    iteration_count += 1