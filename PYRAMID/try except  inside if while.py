def print_pyramid():
    height_input = input("Enter the height of the pyramid: ")

    if height_input.isdigit():
        height = int(height_input)

        try:
            if height > 0:
                i = 1
                while i <= height:
                    spaces = " " * (height - i)
                    stars = "*" * (2 * i - 1)
                    print(spaces + stars)
                    i += 1
            else:
                print("Please enter a positive integer for the height.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Please enter a valid integer for the height.")

# Call the function to print the pyramid
print_pyramid()