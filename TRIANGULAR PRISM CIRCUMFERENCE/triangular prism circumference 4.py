import math

def triangular_prism_properties(a, b, c, h):
    perimeter = a + b + c + 2 * h
    area_base = herons_formula(a, b, c)
    surface_area = area_base * 2 + perimeter * h
    return perimeter, surface_area

def herons_formula(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

while True:
    side_a = input("Enter the length of side a: ")
    side_b = input("Enter the length of side b: ")
    side_c = input("Enter the length of side c: ")
    height = input("Enter the height of the triangular prism: ")

    if side_a.isdigit() and side_b.isdigit() and side_c.isdigit() and height.isdigit():
        side_a, side_b, side_c, height = float(side_a), float(side_b), float(side_c), float(height)

        if side_a > 0 and side_b > 0 and side_c > 0 and height > 0:
            perimeter, surface_area = triangular_prism_properties(side_a, side_b, side_c, height)
            print("Perimeter:", perimeter)
            print("Surface Area:", surface_area)
            break  # Exit the loop if valid input is provided
        else:
            print("Error: All side lengths and height must be positive.")
    else:
        print("Error: Please enter valid positive numerical values.")