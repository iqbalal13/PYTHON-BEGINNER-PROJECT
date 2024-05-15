import math

def cone_perimeter(radius, slant_height, pi_option):
    # Use the selected pi_option for pi value
    pi_value = 22/7 if pi_option == '22/7' else 3.14
    
    # Calculate the circumference of the base
    base_circumference = 2 * pi_value * radius
    
    # Calculate the perimeter of the cone
    perimeter = base_circumference + slant_height
    
    return perimeter

# Get input from the user with input validation using while and if-else
attempt = 0

while True:
    radius_input = input("Enter the radius of the cone base: ")
    slant_height_input = input("Enter the slant height of the cone: ")
    pi_option = input("Choose pi option (22/7 or 3.14): ")

    # Validate radius
    if not radius_input.replace('.', '', 1).isdigit():
        print("Invalid radius input. Please enter a valid numerical value.")
        attempt += 1
        continue

    # Validate slant_height
    if not slant_height_input.replace('.', '', 1).isdigit():
        print("Invalid slant height input. Please enter a valid numerical value.")
        attempt += 1
        continue

    # Validate pi_option
    if pi_option not in ['22/7', '3.14']:
        print("Invalid pi option. Please choose either '22/7' or '3.14'.")
        attempt += 1
        continue

    radius = float(radius_input)
    slant_height = float(slant_height_input)

    break  # Exit the loop if inputs are valid

# Calculate the perimeter using the function
result = cone_perimeter(radius, slant_height, pi_option)

# Display the result
print(f"The perimeter of the cone is: {result}")