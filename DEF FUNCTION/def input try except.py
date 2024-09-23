def divide_numbers():
    try:
        a = float(input("Enter the numerator: "))
        b = float(input("Enter the denominator: "))
        result = a / b
        print("Result:", result)
    except ValueError:
        print("Error: Please enter valid numeric values.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Division successful.")

# Example usage:
divide_numbers()