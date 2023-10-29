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

    try:
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

    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero")