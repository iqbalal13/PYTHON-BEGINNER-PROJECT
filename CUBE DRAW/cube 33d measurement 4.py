def draw_3d_cube(size, unit):
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

    print(f"\nCube Size: {size} {unit}\n")

# Example usage:
try:
    cube_size = int(input("Enter the size of the 3D cube: "))
    unit = input("Enter the unit of measurement (e.g., cm, dm, mm): ")
except ValueError:
    print("Invalid input. Please enter a valid numerical value for the cube size.")
else:
    draw_3d_cube(cube_size, unit)