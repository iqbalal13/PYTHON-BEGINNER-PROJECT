def cube_perimeter(side_length):
    return 4 * side_length

# Example usage with a loop:
for _ in range(3):  # Allow up to 3 attempts
    side_length_input = input("Enter the side length of the cube: ")

    if side_length_input.replace('.', '', 1).isdigit():  # Check if input is a positive number
        side_length = float(side_length_input)

        if side_length > 0:
            perimeter = cube_perimeter(side_length)
            print(f"The perimeter of one face of the cube is: {perimeter}")
            break  # Exit the loop if valid input is received
        else:
            print("Please enter a positive value for the side length.")
    else:
        print("Invalid input. Please enter a valid number.")
else:
    print("Exceeded maximum attempts. Please run the program again.")