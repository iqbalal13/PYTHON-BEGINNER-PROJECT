import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

max_attempts = 3

for attempt in range(max_attempts):
    try:
        radius_input = input(f"Attempt {attempt + 1}: Enter the radius of the sphere: ")
        radius = float(radius_input)

        if radius > 0:
            volume = sphere_volume(radius)
            print(f"The volume of the sphere with radius {radius} is: {volume}")
            break
        elif radius == 0:
            print("The radius should be a positive number.")
        else:
            print("Invalid input. Please enter a positive number for the radius.")
    except ValueError:
        print("Invalid input. Please enter a valid number for the radius.")
else:
    print(f"Exceeded maximum attempts ({max_attempts}). Exiting.")