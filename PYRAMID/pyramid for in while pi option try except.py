import math

def print_pyramid():
    try:
        height_input = input("Enter the height of the pyramid (enter 'quit' to exit): ")

        if height_input.lower() == 'quit':
            print("Exiting the program.")
            return

        height = int(height_input)
        i = 1

        while i <= height:
            if height <= 0:
                print("Please enter a positive integer for the height.")
                break

            pi_option = input("Choose the value of pi (enter '22/7', '3.14', or 'quit' to exit): ").lower()

            if pi_option == 'quit':
                print("Exiting the program.")
                break

            if pi_option == '22/7':
                pi_value = 22 / 7
            elif pi_option == '3.14':
                pi_value = 3.14
            else:
                print("Invalid option for pi. Using the default value 3.14.")
                pi_value = 3.14

            for j in range(1, i + 1):
                print("*", end="")

            print()  # Move to the next line after printing stars

            i += 1

    except ValueError:
        print("Please enter a valid integer for the height.")

# Call the function to print the pyramid
print_pyramid()