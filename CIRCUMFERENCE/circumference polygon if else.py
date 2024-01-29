def prism_circumference_polygon(num_sides, side_length):
    """
    Calculate the circumference of a prism with a regular polygonal base.

    Parameters:
    - num_sides: Number of sides of the base polygon
    - side_length: Length of one side of the base polygon

    Returns:
    - Circumference of the prism
    """
    circumference = num_sides * side_length
    return circumference

# Example usage:
base_type = input("Enter the type of base (polygon): ").lower()

if base_type == "polygon":
    num_sides = int(input("Enter the number of sides of the base polygon: "))
    side_length = float(input("Enter the length of one side of the base polygon: "))
    
    result_polygon = prism_circumference_polygon(num_sides, side_length)
    print("Circumference of the prism with a polygonal base:", result_polygon)
    
else:
    print("Invalid input. Please enter 'polygon' as the base type.")