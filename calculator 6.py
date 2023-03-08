def calculator(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: division by zero")
            return None
        else:
            result = num1 / num2
    else:
        print("Invalid operator")
        return None

    return result

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operator = input("Enter the operator (+, -, *, /): ")

result = calculator(num1, num2, operator)

if result is not None:
    print("Result: ", result)