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
    while True:
        num1_input = input("Enter the first number (or 'exit' to quit): ")

        if num1_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        if not (num1_input.isdigit() or (num1_input[1:].isdigit() and num1_input[0] == '-') or (num1_input.count('.') == 1 and num1_input.replace('.', '').isdigit())):
            print("Error: Please enter a valid first number.")
            continue

        num1 = float(num1_input)

        num2_input = input("Enter the second number: ")
        if not (num2_input.isdigit() or (num2_input[1:].isdigit() and num2_input[0] == '-') or (num2_input.count('.') == 1 and num2_input.replace('.', '').isdigit())):
            print("Error: Please enter a valid second number.")
            continue

        num2 = float(num2_input)

        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            try:
                result = divide(num1, num2)
            except ValueError as ve:
                print(f"Error: {ve}")
                continue
        else:
            print("Error: Invalid operation.")
            continue

        print(f"Result: {result}")

# Example usage:
simple_calculator()