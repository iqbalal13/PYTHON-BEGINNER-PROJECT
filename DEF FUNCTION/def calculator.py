def simple_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Cannot divide by zero.")
                return
        else:
            print("Error: Invalid operation.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
simple_calculator()