def divide_numbers(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("Division successful.")

# Example usage:
divide_numbers(10, 2)  # This should print the result: 5.0 and "Division successful."
divide_numbers(10, 0)  # This should print "Error: Cannot divide by zero."
divide_numbers("abc", 2)  # This should print "An unexpected