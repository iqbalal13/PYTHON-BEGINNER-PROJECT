def calculate_cube_volume_with_tuple(side_length):
    try:
        # Ensure that the side_length is a positive number
        if side_length <= 0:
            raise ValueError("Side length must be a positive number")
        
        # Calculate the volume of the cube
        volume = side_length ** 3
        
        # Return a tuple containing side length and volume
        return side_length, volume

    except ValueError as ve:
        print(f"Error: {ve}")
        return None

# Example usage
try:
    side_length = float(input("Enter the side length of the cube: "))
    result = calculate_cube_volume_with_tuple(side_length)

    if result is not None:
        side_length_result, cube_volume_result = result
        print(f"The volume of the cube with side length {side_length_result} is: {cube_volume_result}")

except ValueError:
    print("Invalid input. Please enter a valid number for the side length.")