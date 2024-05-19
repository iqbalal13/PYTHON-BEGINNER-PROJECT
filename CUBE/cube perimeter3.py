def cube_perimeter(side_length):
    return 4 * side_length

# Example usage with a for loop and without try-except block:
for _ in range(float('inf')):  # Infinite loop with a large number of iterations
    side_length_input = input("Enter the side length of the cube (or type 'quit' to exit): ")

    if side_length_input.lower() == 'quit':
        print("Exiting the program.")
        break

    if side_length_input.replace('.', '', 1).lstrip('-').isdigit():  # Check if input is a positive or negative number
        side_length = float(side_length_input)

        if side_length > 0:
            perimeter = cube_perimeter(side_length)
            print(f"The perimeter of one face of the cube is: {perimeter}")
        else:
            print("Please enter a positive value for the side length.")
    else:
        print("Invalid input. Please enter a valid number.")

