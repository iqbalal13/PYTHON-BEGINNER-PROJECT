import math

def cone_circumference(radius, slant_height, pi_value):
    if radius <= 0 or slant_height <= 0:
        print("Invalid input. Radius and slant height must be positive values.")
        return None
    
    # Choose the value of pi based on the user's input
    if pi_value == "22/7":
        pi = 22/7
    elif pi_value == "3.14":
        pi = 3.14
    else:
        print("Invalid pi_value. Please choose either '22/7' or '3.14'.")
        return None
    
    # Calculate the circumference using the formula
    circumference = 2 * pi * radius + slant_height
    return circumference

max_attempts = 3
attempt = 0

while attempt < max_attempts:
    try:
        user_input = input("Enter the radius, slant height, and pi value (or type 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            print("Exiting the program.")
            break

        radius, slant_height, pi_value = map(str.strip, user_input.split(','))

        radius = float(radius)
        slant_height = float(slant_height)

        result = cone_circumference(radius, slant_height, pi_value)

        if result is not None:
            print(f"The circumference of the cone is: {result}")
            break  # Exit the loop if valid input and calculation are successful
    except ValueError:
        print("Invalid input. Please enter valid numerical values for radius and slant height.")
    
    attempt += 1
    if attempt < max_attempts:
        print(f"You have {max_attempts - attempt} attempts remaining.\n")

print("Maximum attempts reached or user chose to quit. Exiting the program.")