def prism_circumference_circle(radius, pi_approximation):
    """
    Calculate the circumference of a prism with a circular base.

    Parameters:
    - radius: Radius of the circular base
    - pi_approximation: Chosen approximation of pi (3.14 or 22/7)

    Returns:
    - Circumference of the prism
    """
    if pi_approximation == "3.14":
        pi_value = 3.14
    elif pi_approximation == "22/7":
        pi_value = 22 / 7
    else:
        print("Invalid pi approximation. Please choose '3.14' or '22/7'.")
        return None

    circumference = 2 * pi_value * radius
    return circumference

# Example usage:
base_type = input("Enter the type of base (circle): ").lower()

if base_type == "circle":
    base_radius = float(input("Enter the radius of the circular base: "))
    
    pi_choice = input("Choose the approximation of pi (3.14 or 22/7): ").lower()
    
    result_circle = prism_circumference_circle(base_radius, pi_choice)
    
    if result_circle is not None:
        print(f"Circumference of the prism with a circular base (π ≈ {pi_choice}):", result_circle)
else:
    print("Invalid input. Please enter 'circle' as the base type.")