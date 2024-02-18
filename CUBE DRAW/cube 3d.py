def draw_3d_cube(size):
    for i in range(size):
        # Draw the top face
        print(" " * (size - i - 1) + "*" * size)

    for i in range(size - 2, -1, -1):
        # Draw the sides
        print("*" + " " * (size - 2) + "*")

    for i in range(size):
        # Draw the bottom face
        print(" " * i + "*" * (size - i))

# Example usage:
cube_size = int(input("Enter the size of the 3D cube: "))
draw_3d_cube(cube_size)