import math

def sphere_volume(radius, pi=math.pi):
    return (4/3) * pi * radius**3

for _ in range(1, 101):  # Allow up to 100 attempts
    user_input = input("Choose the value of pi (3.14/22/7), enter the radius, or type 'quit' to exit: ")

    if user_input.lower() == 'quit':
        print("Exiting the program. Goodbye!")
        break

    try:
        if user_input == "3.14":
            pi_value = 3.14
        elif user_input == "22/7":
            pi_value = 22/7
        else:
            radius = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number for the radius.")
        continue  # Restart the loop if invalid input is detected

    try:
        if user_input == "3.14" or user_input == "22/7":
            print(f"The volume of the sphere with radius using pi ({pi_value}) is: {sphere_volume(1, pi_value)}")
        elif radius > 0:
            volume = sphere_volume(radius)
            print(f"The volume of the sphere with radius {radius} using the default pi is: {volume}")
        elif radius == 0:
            print("The radius should be a positive number.")
        else:
            print("Invalid input. Please enter a positive number for the radius.")
    except NameError:
        print("Unexpected error. Please try again.")

else:
    print("Exceeded maximum attempts. Exiting.")