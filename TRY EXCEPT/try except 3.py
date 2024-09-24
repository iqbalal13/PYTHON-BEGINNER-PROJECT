try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
    print("The result is:", result)
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")