def triangular_prism_volume(base, height, length):
    volume = 0.5 * base * height * length
    return volume

# Get user input for the dimensions
base_length = float(input("Enter the base length of the triangular prism: "))
height = float(input("Enter the height of the triangular prism: "))
prism_length = float(input("Enter the length of the triangular prism: "))

# Calculate volume
result = triangular_prism_volume(base_length, height, prism_length)

# Display the result
print(f"The volume of the triangular prism is: {result}")