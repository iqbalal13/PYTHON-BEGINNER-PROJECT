def prism_circumference(n, s):
    """
    Calculate the circumference of a prism with a regular polygonal base.

    Parameters:
    - n: Number of sides of the base polygon
    - s: Length of one side of the base polygon

    Returns:
    - Circumference of the prism
    """
    circumference = n * s
    return circumference

# Example usage:
num_sides = 6  # Replace with the actual number of sides of the base polygon
side_length = 3  # Replace with the actual length of one side of the base polygon

result = prism_circumference(num_sides, side_length)
print("Circumference of the prism:", result)