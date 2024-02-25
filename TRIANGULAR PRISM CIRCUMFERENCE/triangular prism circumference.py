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

# Example values
side_a = 5
side_b = 6
side_c = 7
height = 8

perimeter, surface_area = triangular_prism_properties(side_a, side_b, side_c, height)

print("Perimeter:", perimeter)
print("Surface Area:", surface_area)