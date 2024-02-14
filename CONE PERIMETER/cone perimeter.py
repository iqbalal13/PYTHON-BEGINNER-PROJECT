import math

def cone_perimeter(radius, slant_height):
    # Calculate the circumference of the base
    base_circumference = 2 * math.pi * radius
    
    # Calculate the perimeter of the cone
    perimeter = base_circumference + slant_height
    
    return perimeter

# Example usage
radius = 5.0  # Replace with the actual radius of the cone base
slant_height = 8.0  # Replace with the actual slant height of the cone
result = cone_perimeter(radius, slant_height)

print(f"The perimeter of the cone is: {result}")