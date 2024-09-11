# Get user input
user_input = input("Enter a number: ")

# Convert the user input to an integer
user_number = int(user_input)

# Perform conditional checks
if user_number < 0:
    print("The number is negative.")
elif user_number == 0:
    print("The number is zero.")
else:
    print("The number is positive.")