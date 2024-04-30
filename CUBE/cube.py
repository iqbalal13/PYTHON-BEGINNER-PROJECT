def cube_volume(side_length):
    return side_length ** 3

# Example usage:
side_length = float(input("Enter the side length of the cube: "))
volume = cube_volume(side_length)
print(f"The volume of the cube with side length {side_length} is: {volume}")