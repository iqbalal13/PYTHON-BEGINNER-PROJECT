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
for attempt in range(1, float('inf')):
    try:
        radius = float(input("Enter the radius of the cone base: "))
        slant_height = float(input("Enter the slant height of the cone: "))
        pi_option = input("Choose pi option (22/7 or 3.14): ")

        # Validate pi_option
        if pi_option not in ['22/7', '3.14']:
            raise ValueError("Invalid pi option. Please choose either '22/7' or '3.14'.")

        break  # Exit the loop if input is successfully converted to float
    except ValueError as e:
        print(f"Error: {e}")

# Calculate the perimeter using the function
result = cone_perimeter(radius, slant_height, pi_option)

# Display the result
print(f"The perimeter of the cone is: {result}")