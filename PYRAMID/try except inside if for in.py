def print_pyramid():
    height_input = input("Enter the height of the pyramid: ")

    if height_input.isdigit():
        height = int(height_input)
    else:
        print("Please enter a valid integer for the height.")

# Call the function to print the pyramid
print_pyramid()
