def calculator(num1, num2, operator):
    num1 = float(num1)
    num2 = float(num2)
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

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operator = input("Enter the operator (+, -, *, /): ")

result = calculator(num1, num2, operator)

if result is None:
    if operator == '/':
        print("Error: division by zero")
    else:
        print("Invalid operator")
else:
    print("Result: ", result)