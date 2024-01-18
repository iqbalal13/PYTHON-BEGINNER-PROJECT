import math

def print_pyramid():
    while True:
        height_input = input("Enter the height of the pyramid (enter 'quit' to exit): ")

        if height_input.lower() == 'quit':
            print("Exiting the program.")
            break

        if not height_input.isdigit():
            print("Please enter a valid integer for the height.")
            continue

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

            spaces = " " * (height - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)

            i += 1

        if pi_option == 'quit':
            break

        print(f"Using the value of pi: {pi_value}")

# Call the function to print the pyramid
print_pyramid()