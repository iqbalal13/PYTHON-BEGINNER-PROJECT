import math

def cone_perimeter(radius, slant_height):
    # Calculate the circumference of the base
    base_circumference = 2 * math.pi * radius
    
    # Calculate the perimeter of the cone
    perimeter = base_circumference + slant_height
    
    return perimeter

# Get input from the user with input validation using if-else
radius_input = input("Enter the radius of the cone base: ")
slant_height_input = input("Enter the slant height of the cone: ")

if radius_input.replace('.', '', 1).isdigit() and slant_height_input.replace('.', '', 1).isdigit():
    radius = float(radius_input)
    slant_height = float(slant_height_input)

    # Calculate the perimeter using the function
    result = cone_perimeter(radius, slant_height)

    # Display the result
    print(f"The perimeter of the cone is: {result}")
else:
    print("Invalid input. Please enter valid numerical values.")