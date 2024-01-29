import math

def prism_circumference_polygon():
    """
    Calculate the circumference of a prism with a regular polygonal base based on user input.

    Returns:
    - Circumference of the prism
    """
    n = int(input("Enter the number of sides of the base polygon: "))
    s = float(input("Enter the length of one side of the base polygon: "))

    circumference = n * s
    return circumference

def prism_circumference_circle():
    """
    Calculate the circumference of a prism with a circular base based on user input.

    Returns:
    - Circumference of the prism
    """
    radius = float(input("Enter the radius of the circular base: "))

    circumference = 2 * math.pi * radius
    return circumference

# Determine the type of base
base_type = input("Enter the type of base (polygon/circle): ").lower()

if base_type == "polygon":
    result = prism_circumference_polygon()
    print("Circumference of the prism with a polygonal base:", result)
elif base_type == "circle":
    result_circle = prism_circumference_circle()
    print("Circumference of the prism with a circular base:", result_circle)
else:
    print("Invalid input. Please enter 'polygon' or 'circle' as the base type.")