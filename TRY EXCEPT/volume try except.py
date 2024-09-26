def calculate_cube_volume(side_length):
    try:
        # Ensure that the side_length is a positive number
        if side_length <= 0:
            raise ValueError("Side length must be a positive number")
        
        # Calculate the volume of the cube
        volume = side_length ** 3
        return volume

    except ValueError as ve:
        print(f"Error: {ve}")
        return None

# Example usage
try:
    side_length = float(input("Enter the side length of the cube: "))
    cube_volume = calculate_cube_volume(side_length)

    if cube_volume is not None:
        print(f"The volume of the cube with side length {side_length} is: {cube_volume}")

except ValueError:
    print("Invalid input. Please enter a valid number for the side length.")