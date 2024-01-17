def print_pyramid():
    try:
        height = int(input("Enter the height of the pyramid: "))
        
        if height > 0:
            for i in range(1, height + 1):
                spaces = " " * (height - i)
                stars = "*" * (2 * i - 1)
                print(spaces + stars)
        else:
            print("Please enter a positive integer for the height.")
            
    except ValueError:
        print("Please enter a valid integer for the height.")

# Call the function to print the pyramid
print_pyramid()