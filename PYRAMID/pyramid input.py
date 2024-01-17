def print_pyramid():
    try:
        height = int(input("Enter the height of the pyramid: "))
        for i in range(1, height + 1):
            spaces = " " * (height - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)
    except ValueError:
        print("Please enter a valid integer for the height.")

# Call the function to print the pyramid
print_pyramid()