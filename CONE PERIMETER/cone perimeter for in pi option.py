import math

def cone_perimeter(radius, slant_height, use_custom_pi=False, custom_pi=None):
    # Use custom_pi if provided, otherwise use math.pi
    pi_value = custom_pi if use_custom_pi and custom_pi is not None else math.pi
    
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
        use_custom_pi = input("Do you want to use a custom value for pi? (y/n): ").lower() == 'y'
        
        if use_custom_pi:
            custom_pi = float(input("Enter the custom value for pi: "))
        else:
            custom_pi = None

        break  # Exit the loop if input is successfully converted to float
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

# Calculate the perimeter using the function
result = cone_perimeter(radius, slant_height, use_custom_pi, custom_pi)

# Display the result
print(f"The perimeter of the cone is: {result}")