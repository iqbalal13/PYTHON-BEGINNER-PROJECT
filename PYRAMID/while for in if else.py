def print_pyramid():
    while True:
        height_input = input("Enter the height of the pyramid: ")

        if height_input.isdigit():
            height = int(height_input)
            for i in range(1, height + 1):
                spaces = " " * (height - i)
                stars = "*" * (2 * i - 1)
                print(spaces + stars)
            break
        else:
            print("Please enter a valid integer for the height.")

# Call the function to print the pyramid
print_pyramid()