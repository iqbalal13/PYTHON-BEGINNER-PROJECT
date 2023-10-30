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

    if user_input == "add":
        result = int(num1 + num2)
    elif user_input == "sub":
        result = int(num1 - num2)
    elif user_input == "mul":
        result = int(num1 * num2)
    elif user_input == "div" and num2 != 0:
        result = int(num1 / num2)
    elif user_input == "div" and num2 == 0:
        print("Error: Division by zero")
        continue

    if result is not None:
        print("Result:", result)