import math

def sphere_volume(radius, pi=math.pi):
    return (4/3) * pi * radius**3

max_attempts = 3

for attempt in range(max_attempts):
    pi_choice = input("Choose the value of pi (3.14/22/7): ")
    
    if pi_choice == "3.14":
        pi_value = 3.14
    elif pi_choice == "22/7":
        pi_value = 22/7
    else:
        print("Invalid choice. Please enter either '3.14' or '22/7'.")
        continue  # Skip the current iteration if an invalid choice is entered

    radius_input = input(f"Attempt {attempt + 1}: Enter the radius of the sphere: ")
    
    if not radius_input.replace(".", "", 1).isdigit():
        print("Invalid input. Please enter a valid number for the radius.")
        continue  # Skip the current iteration if invalid input is detected

    radius = float(radius_input)

    if radius > 0:
        volume = sphere_volume(radius, pi=pi_value)
        print(f"The volume of the sphere with radius {radius} using pi ({pi_value}) is: {volume}")
        break
    elif radius == 0:
        print("The radius should be a positive number.")
    else:
        print("Invalid input. Please enter a positive number for the radius.")

else:
    print(f"Exceeded maximum attempts ({max_attempts}). Exiting.")