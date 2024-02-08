import math

def cylinder_circumference(radius, pi):
    return 2 * pi * radius

# Example usage with for loop and if-else statement for input validation:
for _ in iter(int, 1):  # Infinite loop using iter and a sentinel value of 1
    radius_input = input("Enter the radius of the cylinder (or type 'quit' to exit): ")

    if radius_input.lower() == 'quit':
        print("Exiting the program.")
        break

    if radius_input.replace('.', '', 1).lstrip('-').isdigit():  # Check if input is a positive or negative number
        radius = float(radius_input)

        pi_option = input("Choose the approximation for π (type '22/7' or '3.14'): ").lower()

        if pi_option == '22/7':
            pi_value = 22/7
        elif pi_option == '3.14':
            pi_value = 3.14
        else:
            print("Invalid option for π. Using the default value (3.14).")
            pi_value = 3.14

        if radius > 0:
            circumference = cylinder_circumference(radius, pi_value)
            print(f"The circumference of the base of the cylinder is: {circumference}")
            break  # Exit the loop if valid input is received
        else:
            print("Please enter a positive value for the radius.")
    else:
        print("Invalid input. Please enter a valid number.")