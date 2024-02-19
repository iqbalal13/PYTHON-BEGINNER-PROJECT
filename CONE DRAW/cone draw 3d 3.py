def draw_3d_cone(height):
    if height <= 0:
        print("Invalid height. Please enter a positive integer.")
        return

    i = 1
    while i <= height:
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars + spaces)
        i += 1

# Example usage with error handling and quit option:
while True:
    user_input = input("Enter the height of the 3D cone (type 'quit' to exit): ")

    if user_input.lower() == 'quit':
        print("Exiting the program.")
        break

    try:
        cone_height = int(user_input)
        if cone_height <= 0:
            raise ValueError("Invalid input. Height must be a positive integer.")
    except ValueError as e:
        print(e)
    else:
        draw_3d_cone(cone_height)