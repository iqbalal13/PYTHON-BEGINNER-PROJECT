try:
    x = int(input("Please enter a number: "))
    print(f"The square of {x} is {x**2}.")
except ValueError:
    print("Invalid input. Please enter a valid number.")