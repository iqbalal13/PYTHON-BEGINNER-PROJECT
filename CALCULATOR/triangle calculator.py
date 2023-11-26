def triangle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilateral Triangle"
        elif a == b or b == c or a == c:
            return "Isosceles Triangle"
        else:
            return "Scalene Triangle"
    else:
        return "Not a valid triangle"

# Example usage:
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

result = triangle_type(side1, side2, side3)
print("Triangle type:", result)