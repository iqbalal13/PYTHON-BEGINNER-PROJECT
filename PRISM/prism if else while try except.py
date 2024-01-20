def draw_prism(length, width, height):
    # Draw the top face
    print(" " * (width + 1) + "_" * length)

    # Draw the sides
    h = height
    while h > 0:
        try:
            if h == height:
                print(" " * h + "/" + " " * (length - 2) + "/")
            elif h == 1:
                raise StopIteration  # Terminate the loop when h equals 1
            else:
                print(" " * h + "/" + " " * (length - 2) + "/")
            h -= 1
        except StopIteration:
            # Draw the bottom face
            print("/" + "_" * (length - 2) + "/")

# Get user input for prism dimensions
length = int(input("Enter the length of the prism: "))
width = int(input("Enter the width of the prism: "))
height = int(input("Enter the height of the prism: "))

# Draw the prism based on user input
draw_prism(length, width, height)