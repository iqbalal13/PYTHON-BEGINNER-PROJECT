
def rectangular_prism_perimeter(length, width, height):
    base_perimeter = 2 * (length + width)
    prism_perimeter = base_perimeter * 4  # Assuming a rectangular prism with 4 sides
    return prism_perimeter

# Example usage
length = float(input("Enter the length of the rectangular base: "))
width = float(input("Enter the width of the rectangular base: "))
height = float(input("Enter the height of the prism: "))

perimeter = rectangular_prism_perimeter(length, width, height)
print(f"The perimeter of the rectangular prism is: {perimeter}")