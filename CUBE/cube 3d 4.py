def draw_3d_cube(size):
    if size <= 0:
        print("Invalid size. Please enter a positive integer.")
        return

    # Draw the top face
    for i in range(size):
        print(" " * (size - i - 1) + "*" * size)

    # Draw the sides
    for i in range(size - 2, -1, -1):
        print("*" + " " * (size - 2) + "*")

    # Draw the bottom face
    for i in range(size):
        print(" " * i + "*" * (size - i))

# Example usage:
cube_size = int(input("Enter the size of the 3D cube: "))
draw_3d_cube(cube_size)