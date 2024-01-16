import math

def sphere_volume(radius, pi=math.pi):
    return (4/3) * pi * radius**3

while True:
    pi_choice = input("Choose the value of pi (3.14/22/7): ")
    
    if pi_choice == "3.14":
        pi_value = 3.14
    elif pi_choice == "22/7":
        pi_value = 22/7
    else:
        print("Invalid choice. Please enter either '3.14' or '22/7'.")
        continue  # Restart the loop if an invalid choice is entered

    radius_input = input("Enter the radius of the sphere: ")
    
    if not radius_input.replace(".", "", 1).isdigit():
        print("Invalid input. Please enter a valid number for the radius.")
        continue  # Restart the loop if invalid input is detected

    radius = float(radius_input)

    if radius > 0:
        volume = sphere_volume(radius, pi=pi_value)
        print(f"The volume of the sphere with radius {radius} using pi ({pi_value}) is: {volume}")
        break
    elif radius == 0:
        print("The radius should be a positive number.")
    else:
        print("Invalid input. Please enter a positive number for the radius.")