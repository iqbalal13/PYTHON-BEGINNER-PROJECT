# Get user input for name and age
name = input("Enter your name: ")
age = input("Enter your age: ")

# Check the age and provide a message
if age.isdigit():  # Check if the age input is a positive integer
    age = int(age)  # Convert the age to an integer
    if age >= 18:
        print(f"Hello, {name}! You are old enough to vote.")
    else:
        print(f"Hello, {name}! You are too young to vote.")
else:
    print("Please enter a valid age as a positive integer.")