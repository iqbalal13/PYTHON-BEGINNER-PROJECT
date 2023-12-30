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
    elif user_input in ("add", "sub", "mul", "div"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "add":
            result = num1 + num2
        elif user_input == "sub":
            result = num1 - num2
        elif user_input == "mul":
            result = num1 * num2
        elif user_input == "div":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero")
                continue

        print("Result: ", result)
    else:
        print("Invalid input. Please enter a valid option.")