# Get user input for name and age
name = input("Enter your name: ")
age = input("Enter your age: ")

if age.isdigit() and int(age) >= 18:
    print(f"Hello, {name}! You are old enough to vote.")
elif age.isdigit():
    print(f"Hello, {name}! You are too young to vote.")
else:
    print("Please enter a valid age as a positive integer.")