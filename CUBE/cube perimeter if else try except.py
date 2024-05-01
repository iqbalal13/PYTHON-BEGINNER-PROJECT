def cube_perimeter(side_length):
    return 4 * side_length

# Example usage:
try:
    side_length = float(input("Enter the side length of the cube: "))
    
    if side_length > 0:
        perimeter = cube_perimeter(side_length)
        print(f"The perimeter of one face of the cube is: {perimeter}")
    else:
        print("Please enter a positive value for the side length.")
except ValueError:
    print("Invalid input. Please enter a valid number.")