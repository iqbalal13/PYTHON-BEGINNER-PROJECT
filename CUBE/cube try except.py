def cube_volume(side_length):
    if side_length > 0:
        return side_length ** 3
    else:
        print("Invalid input. The side length should be a positive number.")
        return None  # Returning None or another value to indicate an error

try:
    side_length = float(input("Enter the side length of the cube: "))
    volume = cube_volume(side_length)

    if volume is not None:
        print(f"The volume of the cube with side length {side_length} is: {volume}")
except ValueError:
    print("Invalid input. Please enter a valid number for the side length.")