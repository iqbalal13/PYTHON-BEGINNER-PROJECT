def cube_volume(side_length):
    if side_length > 0:
        return side_length ** 3
    else:
        print("Invalid input. The side length should be a positive number.")
        return None  # Returning None or another value to indicate an error

max_attempts = 3

for attempt in range(max_attempts):
    try:
        side_length = float(input("Enter the side length of the cube: "))
        volume = cube_volume(side_length)

        if volume is not None:
            print(f"The volume of the cube with side length {side_length} is: {volume}")
            break  # Exit the loop if a valid input is provided
    except ValueError:
        print("Invalid input. Please enter a valid number for the side length.")
    else:
        if attempt < max_attempts - 1:
            print(f"You have {max_attempts - attempt - 1} attempts remaining.")
else:
    print(f"Exceeded maximum attempts ({max_attempts}). Exiting.")