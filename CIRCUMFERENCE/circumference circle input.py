import math

def prism_circumference_circle():
    """
    Calculate the circumference of a prism with a circular base based on user input.

    Returns:
    - Circumference of the prism
    """
    radius = float(input("Enter the radius of the circular base: "))

    circumference = 2 * math.pi * radius
    return circumference

# Example usage:
result_circle = prism_circumference_circle()
print("Circumference of the prism with a circular base:", result_circle)