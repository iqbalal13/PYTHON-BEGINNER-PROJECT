def prism_circumference():
    """
    Calculate the circumference of a prism with a regular polygonal base based on user input.

    Returns:
    - Circumference of the prism
    """
    n = int(input("Enter the number of sides of the base polygon: "))
    s = float(input("Enter the length of one side of the base polygon: "))

    circumference = n * s
    return circumference

# Example usage:
result = prism_circumference()
print("Circumference of the prism:", result)