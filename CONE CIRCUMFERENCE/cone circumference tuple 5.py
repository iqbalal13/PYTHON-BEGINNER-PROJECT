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

for _ in range(1):  # A single iteration, equivalent to while True
    user_input = input("Enter the radius, slant height, and pi value (or type 'quit' to exit): ")
    
    if user_input.lower() == 'quit':
        print("Exiting the program.")
        break

    inputs = tuple(map(str.strip, user_input.split(',')))

    if len(inputs) == 3 and all(value.replace('.', '').isdigit() for value in inputs):
        inputs = tuple(float(value) for value in inputs)
        result = cone_circumference(inputs)
        
        if result is not None:
            print(f"The circumference of the cone is: {result}")
    else:
        print("Invalid input. Please enter three numeric values separated by commas.")