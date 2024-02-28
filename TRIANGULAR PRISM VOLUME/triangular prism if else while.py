def triangular_prism_volume(base, height, length):
    volume = 0.5 * base * height * length
    return volume

# Get user input for the dimensions with input validation
while True:
    base_length = float(input("Enter the base length of the triangular prism: "))
    height = float(input("Enter the height of the triangular prism: "))
    prism_length = float(input("Enter the length of the triangular prism: "))

    # Input validation
    if base_length >= 0 and height >= 0 and prism_length >= 0:
        break
    else:
        print("Please enter non-negative values for all dimensions.")

# Calculate volume
result = triangular_prism_volume(base_length, height, prism_length)

# Display the result
print(f"The volume of the triangular prism is: {result}")