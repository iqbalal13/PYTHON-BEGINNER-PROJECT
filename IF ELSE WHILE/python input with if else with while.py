while True:
    name = input("Enter your name: ")
    age = input("Enter your age: ")

    if age.isdigit() and int(age) >= 18:
        print(f"Hello, {name}! You are old enough to vote.")
    elif age.isdigit():
        print(f"Hello, {name}! You are too young to vote.")
    else:
        print("Please enter a valid age as a positive integer.")

    another_entry = input("Do you want to check another name and age? (yes/no): ")
    if another_entry.lower() != "yes":
        break