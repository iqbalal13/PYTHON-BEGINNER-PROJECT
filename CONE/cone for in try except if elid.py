import math

def cone_volume(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume

# Get user input for radius with error handling using try-except and for loop
max_attempts = 3
for attempt in range(max_attempts):
    try:
        radius_input = input("Enter the radius of the cone: ")
        radius = float(radius_input)

        if radius > 0:
            break
        else:
            print("Radius must be a positive number.")
    except ValueError as ve:
        print(f"Invalid input for radius: {ve}")

else:
    print(f"Exceeded {max_attempts} attempts for radius. Exiting.")
    exit()

# Get user input for height with error handling using try-except and for loop
for attempt in range(max_attempts):
    try:
        height_input = input("Enter the height of the cone: ")
        height = float(height_input)

        if height > 0:
            break
        else:
            print("Height must be a positive number.")
    except ValueError as ve:
        print(f"Invalid input for height: {ve}")

else:
    print(f"Exceeded {max_attempts} attempts for height. Exiting.")
    exit()

# Calculate the volume using the function
result = cone_volume(radius, height)

# Display the result
print(f"The volume of the cone with radius {radius} and height {height} is: {result}")