def cube_volume(side_length):
    if side_length > 0:
        return side_length ** 3
    else:
        print("Invalid input. The side length should be a positive number.")
        return None  # Returning None or another value to indicate an error

max_attempts = float('inf')
score = 0

for attempt in range(max_attempts):
    try:
        user_input = input("Enter the side length of the cube, or type 'exit' to quit: ")

        if user_input.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break  # Exit the outer loop if 'exit' is entered
        
        side_length = float(user_input)

        if side_length > 0:
            volume = cube_volume(side_length)
            print(f"The volume of the cube with side length {side_length} is: {volume}")
            score += 1  # Increment the score for a successful attempt
            print(f"Your current score is: {score}")
            break  # Exit the outer loop if a valid input is provided
        else:
            print("Invalid input. The side length should be a positive number.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the side length.")
    else:
        print("You can keep entering side lengths or type 'exit' to quit.")

print("Exiting the program.")