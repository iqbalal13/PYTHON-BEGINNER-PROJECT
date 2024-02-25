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

# User input
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
side_c = float(input("Enter the length of side c: "))
height = float(input("Enter the height of the triangular prism: "))

perimeter, surface_area = triangular_prism_properties(side_a, side_b, side_c, height)

print("Perimeter:", perimeter)
print("Surface Area:", surface_area)