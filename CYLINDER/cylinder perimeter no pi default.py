import math

def cylinder_circumference(radius, pi):
    return 2 * pi * radius

# Example usage with for loop, try-except block, and if-else statement for input validation:
for _ in iter(int, 1):  # Infinite loop using iter and a sentinel value of 1
    try:
        radius_input = input("Enter the radius of the cylinder (or type 'quit' to exit): ")

        if radius_input.lower() == 'quit':
            print("Exiting the program.")
            break

        radius = float(radius_input)

        pi_option = input("Choose the approximation for π (type '22/7' or '3.14'): ").lower()

        if pi_option == '22/7':
            pi_value = 22/7
        elif pi_option == '3.14':
            pi_value = 3.14
        else:
            print("Invalid option for π. Exiting the program.")
            break

        if radius > 0:
            circumference = cylinder_circumference(radius, pi_value)
            print(f"The circumference of the base of the cylinder is: {circumference}")
        else:
            print("Please enter a positive value for the radius.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("Exiting the program.")