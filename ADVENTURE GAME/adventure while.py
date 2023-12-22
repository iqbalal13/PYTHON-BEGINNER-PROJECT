import time

print("Welcome to the Simple Adventure Game!")
time.sleep(1)
print("You find yourself standing at a crossroad.")
time.sleep(1)
print("Make a choice to determine your destiny.")

# First choice
choices = ["Go left", "Go right"]
attempts = 0
while attempts < 3:  # Allow three attempts
    user_input = input("\nChoose an option:\n1. Go left\n2. Go right\nEnter the number of your choice: ")

    if user_input.isdigit():
        choice = int(user_input)
        if 1 <= choice <= len(choices):
            break
        else:
            print("Invalid choice. Please enter a valid number.")
    else:
        print("Invalid input. Please enter a number.")

    attempts += 1

else:
    print("Too many invalid attempts. Exiting.")
    exit()

if choice == 1:
    print("\nYou chose to go left.")
    time.sleep(1)
    print("You encounter a mystical forest.")
    time.sleep(1)
    print("A fairy offers you a magical potion. Do you accept?")
    
    choices = ["Yes", "No"]
    attempts = 0
    while attempts < 3:
        user_input = input("\nEnter the number of your choice:\n1. Yes\n2. No\nYour choice: ")

        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= len(choices):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        else:
            print("Invalid input. Please enter a number.")

        attempts += 1

    else:
        print("Too many invalid attempts. Exiting.")
        exit()

    if choice == 1:
        print("\nYou accept the potion and feel a surge of magical energy.")
        time.sleep(1)
        print("The fairy guides you safely through the forest.")
    else:
        print("\nYou decline the potion and cautiously navigate the forest.")
        time.sleep(1)
        print("You emerge safely on the other side.")

else:
    print("\nYou chose to go right.")
    time.sleep(1)
    print("You find a treasure chest.")
    time.sleep(1)
    print("Do you open the chest?")

    choices = ["Yes", "No"]
    attempts = 0
    while attempts < 3:
        user_input = input("\nEnter the number of your choice:\n1. Yes\n2. No\nYour choice: ")

        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= len(choices):
                break
            else:
                print("Invalid choice. Please enter a valid number.")
        else:
            print("Invalid input. Please enter a number.")

        attempts += 1

    else:
        print("Too many invalid attempts. Exiting.")
        exit()

    if choice == 1:
        print("\nYou open the chest and find a pile of gold coins.")
        time.sleep(1)
        print("Congratulations! You're rich!")
    else:
        print("\nYou decide not to open the chest and continue your journey.")

print("\nThanks for playing the Simple Adventure Game!")