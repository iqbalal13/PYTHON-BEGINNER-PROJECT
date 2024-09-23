def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

def simple_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

        if operation in operations:
            result = operations[operation](num1, num2)
            print(f"Result: {result}")
        else:
            print("Error: Invalid operation.")

    except ValueError:
        print("Error: Please enter valid numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
simple_calculator()