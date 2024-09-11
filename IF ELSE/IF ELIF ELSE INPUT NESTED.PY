user_input = input("Enter a number: ")

if user_input.isdigit():
    number = int(user_input)
    
    if number > 0:
        print("You entered a positive number.")
    elif number < 0:
        print("You entered a negative number.")
    else:
        print("You entered zero.")
else:
    print("Invalid input. Please enter a valid number.")