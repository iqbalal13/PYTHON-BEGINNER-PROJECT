def print_pyramid():
    try:
        height = int(input("Enter the height of the pyramid: "))
        
        i = 1
        while i <= height:
            spaces = " " * (height - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)
            i += 1
    except ValueError:
        print("Please enter a valid integer for the height.")

# Call the function to print the pyramid
print_pyramid()