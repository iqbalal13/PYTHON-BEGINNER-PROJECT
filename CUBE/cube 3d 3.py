def draw_3d_cube(size):
    if size <= 0:
        print("Invalid size. Please enter a positive integer.")
        return

    i = 0
    while i < size:
        # Draw the top face
        print(" " * (size - i - 1) + "*" * size)
        i += 1

    i = size - 2
    while i >= 0:
        # Draw the sides
        print("*" + " " * (size - 2) + "*")
        i -= 1

    i = 0
    while i < size:
        # Draw the bottom face
        print(" " * i + "*" * (size - i))
        i += 1

# Example usage:
cube_size = int(input("Enter the size of the 3D cube: "))
draw_3d_cube(cube_size)