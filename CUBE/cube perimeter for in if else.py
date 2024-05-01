def cube_perimeter(side_length):
    return 4 * side_length

# Example usage with a while loop:
max_attempts = 3
attempts = 0

while attempts < max_attempts:
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

    attempts += 1

if attempts == max_attempts:
    print("Exceeded maximum attempts. Please run the program again.")