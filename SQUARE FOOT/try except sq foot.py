try:
    # Get user input for length and width
    length = float(input("Enter the length of the room in feet: "))
    width = float(input("Enter the width of the room in feet: "))
    
    # Create a tuple with the dimensions
    room_dimensions = (length, width)

    # Calculate square footage
    square_footage = room_dimensions[0] * room_dimensions[1]

    # Print the result
    print(f"The square footage of the room is: {square_footage} square feet")

except ValueError:
    print("Invalid input. Please enter valid numerical values for length and width.")