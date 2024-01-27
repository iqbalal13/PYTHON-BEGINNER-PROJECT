import math

def prism_circumference_circle(radius):
    """
    Calculate the circumference of a prism with a circular base.

    Parameters:
    - radius: Radius of the circular base

    Returns:
    - Circumference of the prism
    """
    circumference = 2 * math.pi * radius
    return circumference

# Example usage:
base_radius = 5  # Replace with the actual radius of the circular base

result_circle = prism_circumference_circle(base_radius)
print("Circumference of the prism with a circular base:", result_circle)