while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'sub' for subtraction")
    print("Enter 'mul' for multiplication")
    print("Enter 'div' for division")
    print("Enter 'exit' to end the program")
    
    user_input = input(": ")

    if user_input == "exit":
        break

    if user_input not in ("add", "sub", "mul", "div"):
        print("Invalid input. Please enter a valid option.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = None

    for operation in ["add", "sub", "mul", "div"]:
        if user_input == operation:
            if operation == "add":
                result = num1 + num2
            elif operation == "sub":
                result = num1 - num2
            elif operation == "mul":
                result = num1 * num2
            elif operation == "div":
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero")
                    break

    if result is not None:
        print("Result: ", result)