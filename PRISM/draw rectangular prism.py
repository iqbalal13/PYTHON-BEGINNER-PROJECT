def draw_rectangular_prism(width, height, depth):
    for i in range(height):
        for j in range(width):
            print("/", end="")
        print()

    for k in range(depth - 2):
        print("|" + " " * (width - 2) + "|")

    for i in range(height):
        for j in range(width):
            print("\\", end="")
        print()