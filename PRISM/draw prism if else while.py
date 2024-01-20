def draw_prism(length, width, height):
    # Draw the top face
    print(" " * (width + 1) + "_" * length)
    
    # Draw the sides
    while height > 0:
        print(" " * height + "/" + " " * (length - 2) + "/")
        height -= 1
    else:
        # Draw the bottom face
        print("/" + "_" * (length - 2) + "/")

# Get user input for prism dimensions
length = int(input("Enter the length of the prism: "))
width = int(input("Enter the width of the prism: "))
height = int(input("Enter the height of the prism: "))

# Draw the prism based on user input
draw_prism(length, width, height)