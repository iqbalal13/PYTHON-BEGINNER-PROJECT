length_input = input("Enter the length of the room in feet: ")
if length_input.replace('.', '', 1).isdigit():  # Check if input is a valid float
    length = float(length_input)
    
    # Get user input for width
    width_input = input("Enter the width of the room in feet: ")
    if width_input.replace('.', '', 1).isdigit():  # Check if input is a valid float
        width = float(width_input)
        
        # Create a tuple with the dimensions
        room_dimensions = (length, width)

        # Calculate square footage
        square_footage = room_dimensions[0] * room_dimensions[1]

        # Print the result
        print(f"The square footage of the room is: {square_footage} square feet")
    else:
        print("Invalid input for width. Please enter a valid numerical value.")
else:
    print("Invalid input for length. Please enter a valid numerical value.")