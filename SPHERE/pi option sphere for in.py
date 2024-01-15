import math

def sphere_volume(radius, pi=math.pi):
    return (4/3) * pi * radius**3

max_attempts = 3

for attempt in range(max_attempts):
    try:
        use_default_pi = input("Do you want to use the default value of pi? (y/n): ").lower() == 'y'

        if use_default_pi:
            radius_input = input(f"Attempt {attempt + 1}: Enter the radius of the sphere: ")
            radius = float(radius_input)
            volume = sphere_volume(radius)
            print(f"The volume of the sphere with radius {radius} is: {volume}")
            break
        else:
            custom_pi = float(input("Enter your custom value for pi: "))
            radius_input = input(f"Attempt {attempt + 1}: Enter the radius of the sphere: ")
            radius = float(radius_input)
            volume = sphere_volume(radius, pi=custom_pi)
            print(f"The volume of the sphere with radius {radius} using custom pi ({custom_pi}) is: {volume}")
            break
    except ValueError:
        print("Invalid input. Please enter a valid number for the radius.")
else:
    print(f"Exceeded maximum attempts ({max_attempts}). Exiting.")