import math

def draw_cone(height):
    if height <= 0:
        print("Invalid height. Please enter a positive integer.")
        return

    for i in range(1, height + 1):
        spaces = " " * (height - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

# Example usage:
cone_height = int(input("Enter the height of the cone: "))
draw_cone(cone_height)