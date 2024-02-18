def draw_cube(side_length):
    # Top face
    for _ in range(side_length):
        print('* ' * side_length)

    print()  # Add a newline for separation

    # Side faces
    for _ in range(side_length - 2):
        print('* ' + '  ' * (side_length - 2) + '*')

    print()  # Add a newline for separation

    # Bottom face
    for _ in range(side_length):
        print('* ' * side_length)

# Example usage:
side_length = int(input("Enter the side length of the cube: "))
draw_cube(side_length)