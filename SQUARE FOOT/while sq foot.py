length = None
width = None

# Get user input for length
while length is None:
    length_input = input("Enter the length of the room in feet: ")
    if length_input.replace('.', '', 1).isdigit():
        length = float(length_input)
    else:
        print("Invalid input for length. Please enter a valid numerical value.")

# Get user input for width
while width is None:
    width_input = input("Enter the width of the room in feet: ")
    if width_input.replace('.', '', 1).isdigit():
        width = float(width_input)
    else:
        print("Invalid input for width. Please enter a valid numerical value.")

# Create a tuple with the dimensions
room_dimensions = (length, width)

# Calculate square footage
square_footage = room_dimensions[0] * room_dimensions[1]

# Print the result