def calculator(num1, num2, operator):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return None
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            return None
        else:
            result = num1 / num2
    else:
        return None

    return result

num1_input = input("Enter the first number: ")
num2_input = input("Enter the second number: ")
operator = input("Enter the operator (+, -, *, /): ")

try:
    num1 = float(num1_input)
    num2 = float(num2_input)
except ValueError:
    print("Error: invalid input")
    exit()

result = calculator(num1, num2, operator)

if result is None:
    if operator == '/':
        print("Error: division by zero")
    else:
        print("Invalid operator")
else:
    print("Result: ", result)