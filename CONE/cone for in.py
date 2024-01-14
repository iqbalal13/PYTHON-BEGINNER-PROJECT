import math

def cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

# Initialize variables
max_attempts = 3

# Get user input for radius with error handling using a for loop
for attempt in range(max_attempts):
    radius_input = input("Enter the radius of the cone: ")
    if radius_input.replace('.', '', 1).isdigit():
        radius = float(radius_input)
        break  # Break out of the loop if valid input is provided
    else:
        print("Invalid input. Please enter a numeric value for the radius.")
else:
    print(f"Exceeded {max_attempts} attempts. Exiting.")
    exit()

# Get user input for height with error handling using a for loop
for attempt in range(max_attempts):
    height_input = input("Enter the height of the cone: ")
    if height_input.replace('.', '', 1).isdigit():
        height = float(height_input)
        break  # Break out of the loop if valid input is provided
    else:
        print("Invalid input. Please enter a numeric value for the height.")
else:
    print(f"Exceeded {max_attempts} attempts. Exiting.")
    exit()

# Calculate the volume using the function
result = cone_volume(radius, height)

# Display the result
print(f"The volume of the cone with radius {radius} and height {height} is: {result}")