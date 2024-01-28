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
base_type = input("Enter the type of base (circle): ").lower()

if base_type == "circle":
    base_radius = float(input("Enter the radius of the circular base: "))
    result_circle = prism_circumference_circle(base_radius)
    print("Circumference of the prism with a circular base:", result_circle)
else:
    print("Invalid input. Please enter 'circle' as the base type.")