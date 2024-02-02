import math

def cone_circumference(inputs):
    radius, slant_height, pi_value = inputs

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

for attempt in range(1, max_attempts + 1):
    try:
        user_input = input("Enter the radius, slant height, and pi value (or type 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            print("Exiting the program.")
            break

        inputs = tuple(map(str.strip, user_input.split(',')))

        if len(inputs) != 3:
            print("Invalid input. Please enter three values separated by commas.")
            continue

        inputs = tuple(float(value) for value in inputs)
        
        result = cone_circumference(inputs)

        if result is not None:
            print(f"The circumference of the cone is: {result}")
            break  # Exit the loop if valid input and calculation are successful
    except ValueError:
        print("Invalid input. Please enter valid numerical values for radius and slant height.")
    
    if attempt < max_attempts:
        print(f"You have {max_attempts - attempt} attempts remaining.\n")

print("Maximum attempts reached or user chose to quit. Exiting the program.")