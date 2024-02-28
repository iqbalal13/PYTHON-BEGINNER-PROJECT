def triangular_prism_volume(base, height, length):
    volume = 0.5 * base * height * length
    return volume

max_attempts = 3  # You can adjust the maximum number of attempts

# Get user input for the dimensions with input validation using try-except
for attempt in range(1, max_attempts + 1):
    try:
        base_length = float(input("Enter the base length of the triangular prism: "))
        height = float(input("Enter the height of the triangular prism: "))
        prism_length = float(input("Enter the length of the triangular prism: "))

        # Input validation
        if base_length < 0 or height < 0 or prism_length < 0:
            raise ValueError("Please enter non-negative values for all dimensions.")

        # Calculate volume
        result = triangular_prism_volume(base_length, height, prism_length)
        # Display the result
        print(f"The volume of the triangular prism is: {result}")
        break

    except ValueError as e:
        print(f"Attempt {attempt}/{max_attempts}: {e}")

if attempt == max_attempts:
    print("Maximum attempts reached. Exiting.")