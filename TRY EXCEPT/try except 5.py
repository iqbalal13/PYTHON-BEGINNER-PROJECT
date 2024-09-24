try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
except:
    print("An error occurred.")
else:
    print("The result is:", result)
finally:
    print("Thank you for using this program.")