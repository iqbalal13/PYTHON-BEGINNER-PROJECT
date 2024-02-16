import math

def cone_perimeter(radius, slant_height, pi_option, unit):
    # Use the selected pi_option for pi value
    pi_value = 22/7 if pi_option == '22/7' else 3.14
    
    # Calculate the circumference of the base
    base_circumference = 2 * pi_value * radius
    
    # Calculate the perimeter of the cone
    perimeter = base_circumference + slant_height

    # Convert the result to the selected unit
    if unit == 'cm':
        perimeter *= 100  # Convert to centimeters
    elif unit == 'dm':
        perimeter *= 10   # Convert to decimeters
    elif unit == 'mm':
        perimeter *= 1000  # Convert to millimeters

    # Append the unit to the result
    result_with_unit = f"{perimeter} {unit}"
    
    return result_with_unit

# Get input from the user with input validation using while and try-except
while True:
    try:
        radius_input = input("Enter the radius of the cone base: ")
        slant_height_input = input("Enter the slant height of the cone: ")
        pi_option = input("Choose pi option (22/7 or 3.14): ")
        unit = input("Choose the measurement unit (cm, dm, mm): ")

        # Validate radius
        radius = float(radius_input)

        # Validate slant_height
        slant_height = float(slant_height_input)

        # Validate pi_option
        if pi_option not in ['22/7', '3.14']:
            raise ValueError("Invalid pi option. Please choose either '22/7' or '3.14'.")

        # Validate unit
        if unit not in ['cm', 'dm', 'mm']:
            raise ValueError("Invalid unit. Please choose either 'cm', 'dm', or 'mm'.")

        break  # Exit the loop if inputs are valid

    except ValueError as e:
        print(f"Error: {e}")

# Calculate the perimeter using the function
result = cone_perimeter(radius, slant_height, pi_option, unit)

# Display the result
print(f"The perimeter of the cone is: {result}")