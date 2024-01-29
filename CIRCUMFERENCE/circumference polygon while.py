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

# Example usage with a while loop:
while True:
    base_type = input("Enter the type of base (polygon) or 'exit' to end: ").lower()

    if base_type == "exit":
        break
    
    if base_type == "polygon":
        num_sides = int(input("Enter the number of sides of the base polygon: "))
        side_length = float(input("Enter the length of one side of the base polygon: "))
        
        result_polygon = prism_circumference_polygon(num_sides, side_length)
        print("Circumference of the prism with a polygonal base:", result_polygon)
        
    else:
        print("Invalid input. Please enter 'polygon' or 'exit'.")

# The program will continue running until the user enters 'exit'.