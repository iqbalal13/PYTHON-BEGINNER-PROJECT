import math

def cone_perimeter(radius, slant_height, pi_option, unit):
    # Use the selected pi_option for pi value
    pi_value = 22/7 if pi_option == '22/7' else 3.14
    
    # Calculate the circumference of the base
    base_circumference = 2 * pi_value * radius
    
    # Calculate the perimeter of the cone and convert to the selected unit
    perimeter = (base_circumference + slant_height) * \
                (100 if unit == 'cm' else 10 if unit == 'dm' else 1000)

    # Display the result
    print(f"The perimeter of the cone is: {perimeter} {unit}")

# Main loop
while True:
    # Get input from the user
    radius_input = input("Enter the radius of the cone base (type 'quit' to exit): ")

    # Check for quit condition
    if radius_input.lower() == 'quit':
        print("Exiting the program.")
        break  # Exit the loop if the user decides to quit

    # Validate radius
    if not radius_input.replace('.', '', 1).isdigit():
        print("Invalid radius input. Please enter a valid numerical value.")
        continue

    radius = float(radius_input)

    # Get additional input
    slant_height_input = input("Enter the slant height of the cone: ")
    pi_option = input("Choose pi option (22/7 or 3.14): ")
    unit = input("Choose the measurement unit (cm, dm, mm): ")

    # Validate slant_height
    if not slant_height_input.replace('.', '', 1).isdigit():
        print("Invalid slant height input. Please enter a valid numerical value.")
        continue

    slant_height = float(slant_height_input)

    # Validate pi_option
    if pi_option not in ['22/7', '3.14']:
        print("Invalid pi option. Please choose either '22/7' or '3.14'.")
        continue

    # Validate unit
    if unit not in ['cm', 'dm', 'mm']:
        print("Invalid unit. Please choose either 'cm', 'dm', or 'mm'.")
        continue

    # Calculate and display the perimeter using the function
    cone_perimeter(radius, slant_height, pi_option, unit)