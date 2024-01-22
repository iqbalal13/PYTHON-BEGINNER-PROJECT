def triangular_prism_volume(base, height, length):
    volume = 0.5 * base * height * length
    return volume

max_attempts = float('inf')  # Use a large number for an effectively infinite loop

# Get user input for the dimensions with input validation using while loop
attempt = 1
while attempt <= max_attempts:
    user_input = input("Enter the base length, height, and length of the triangular prism (or type 'quit' to exit): ")

    if user_input.lower() == 'quit':
        print("Exiting the program.")
        break

    input_values = user_input.split()
    
    if len(input_values) != 3:
        print(f"Attempt {attempt}: Error: Please enter three values.")
    else:
        try:
            base_length, height, prism_length = map(float, input_values)
            
            # Input validation
            if base_length < 0 or height < 0 or prism_length < 0:
                raise ValueError("Please enter non-negative values for all dimensions.")

            # Calculate volume
            result = triangular_prism_volume(base_length, height, prism_length)
            # Display the result
            print(f"The volume of the triangular prism is: {result}")

        except ValueError as e:
            print(f"Attempt {attempt}: Error: {e}. Please enter valid numeric values.")

    attempt += 1