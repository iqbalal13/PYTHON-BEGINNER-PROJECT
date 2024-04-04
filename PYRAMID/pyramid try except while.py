def print_pyramid():
    try:
        height = int(input("Enter the height of the pyramid: "))
    
    except ValueError:
        print("Please enter a valid integer for the height.")

# Call the function to print the pyramid
print_pyramid()
