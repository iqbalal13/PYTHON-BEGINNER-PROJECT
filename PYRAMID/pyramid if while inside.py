def print_pyramid():
    height_input = input("Enter the height of the pyramid: ")

    if height_input.isdigit():
        height = int(height_input)

        i = 1
        while i <= height:
            spaces = " " * (height - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)
            i += 1
    else:
        print("Please enter a valid integer for the height.")

# Call the function to print the pyramid