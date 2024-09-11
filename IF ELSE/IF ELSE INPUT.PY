user_input = input("Enter a number: ")

if user_input.isdigit():
    # The input is a valid number
    number = int(user_input)
    print("You entered a valid number:", number)
else:
    # The input is not a number
    print("Invalid input. Please enter a valid number.")