import math

def cylinder_circumference(radius):
    return 2 * math.pi * radius

# Example usage with for loop and if-else statement for input validation:
for _ in range(3):  # Allow up to 3 attempts
    radius_input = input("Enter the radius of the cylinder (or type 'quit' to exit): ")

    if radius_input.lower() == 'quit':
        print("Exiting the program.")
        break

    if radius_input.replace('.', '', 1).lstrip('-').isdigit():  # Check if input is a positive or negative number
        radius = float(radius_input)

        if radius > 0:
            circumference = cylinder_circumference(radius)
            print(f"The circumference of the base of the cylinder is: {circumference}")
            break  # Exit the loop if valid input is received
        else:
            print("Please enter a positive value for the radius.")
    else:
        print("Invalid input. Please enter a valid number.")
else:
    print("Exceeded maximum attempts. Please run the program again.")