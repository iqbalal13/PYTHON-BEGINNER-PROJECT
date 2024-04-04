import math

def print_pyramid():
    height_input = input("Enter the height of the pyramid: ")

    if height_input.isdigit():
        height = int(height_input)

        try:
            if height > 0:
                pi_option = input("Choose the value of pi (enter '22/7' or '3.14'): ").lower()

                if pi_option == '22/7':
                    pi_value = 22 / 7
                elif pi_option == '3.14':
                    pi_value = 3.14
                else:
                    print("Invalid option for pi. Using the default value 3.14.")
                    pi_value = 3.14
            else:
                print("Please enter a positive integer for the height.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Please enter a valid integer for the height.")

# Call the function to print the pyramid
print_pyramid()
