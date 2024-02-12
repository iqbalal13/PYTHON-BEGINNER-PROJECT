import math

def prism_perimeter(length, width, height, base_shape, use_pi=True):
    if base_shape == "rectangle":
        base_perimeter = 2 * (length + width)
        prism_perimeter = base_perimeter * 4  # Assuming a rectangular prism with 4 sides
        return prism_perimeter
    elif base_shape == "triangle":
        # Perimeter of a triangle = sum of all three sides
        base_perimeter = length + width + height
        prism_perimeter = base_perimeter * 3  # Assuming a triangular prism with 3 sides
        return prism_perimeter
    elif base_shape == "circle":
        # Circumference of a circle = 2 * π * radius
        if use_pi:
            base_perimeter = 2 * math.pi * length
        else:
            pi_value = float(input("Enter the value of pi: "))
            base_perimeter = 2 * pi_value * length
        prism_perimeter = base_perimeter  # Assuming a cylindrical prism with a circular base
        return prism_perimeter
    else:
        print("Base shape not supported")
        return None

num_iterations = int(input("Enter the maximum number of prisms you want to calculate (enter 0 to quit): "))

iteration_count = 0

while iteration_count < num_iterations:
    try:
        option = input("Enter 'calculate' to compute the prism perimeter, or 'quit' to exit: ")

        if option.lower() == 'quit':
            break

        if option.lower() == 'calculate':
            base_shape = input("Enter the base shape of the prism (rectangle, triangle, circle, etc.): ")

            if base_shape == "rectangle" or base_shape == "triangle" or base_shape == "circle":
                use_pi = input("Do you want to use the value of pi? (yes/no): ").lower() == 'yes'

                if base_shape == "circle":
                    radius = float(input("Enter the radius of the circular base: "))
                    perimeter = prism_perimeter(radius, 0, 0, base_shape, use_pi)  # Only radius is needed for a circle
                else:
                    length = float(input("Enter the length of the base: "))
                    width = float(input("Enter the width of the base: "))
                    height = float(input("Enter the height of the prism: "))
                    perimeter = prism_perimeter(length, width, height, base_shape, use_pi)
                
                if perimeter is not None:
                    print(f"The perimeter of the prism with {base_shape} base is: {perimeter}")

                iteration_count += 1
            else:
                print("Base shape not supported")

        else:
            print("Invalid option. Please enter 'calculate' or 'quit'.")

    except ValueError:
        print("Invalid input. Please enter valid numerical values for dimensions.")
    except Exception as e:
        print(f"An error occurred: {e}")