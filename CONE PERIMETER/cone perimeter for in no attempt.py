import math

def cone_perimeter(radius, slant_height):
    # Calculate the circumference of the base
    base_circumference = 2 * math.pi * radius
    
    # Calculate the perimeter of the cone
    perimeter = base_circumference + slant_height
    
    return perimeter

# Get input from the user with input validation using while and if-else
for attempt in range(1, float('inf')):
    try:
        radius = float(input("Enter the radius of the cone base: "))
        slant_height = float(input("Enter the slant height of the cone: "))
        break  # Exit the loop if input is successfully converted to float
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

# Calculate the perimeter using the function
result = cone_perimeter(radius, slant_height)

# Display the result
print(f"The perimeter of the cone is: {result}")