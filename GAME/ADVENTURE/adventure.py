import time

def introduction():
    print("Welcome to the Simple Adventure Game!")
    time.sleep(1)
    print("You find yourself standing at a crossroad.")
    time.sleep(1)
    print("Make a choice to determine your destiny.")

def make_choice(choices):
    print("\nChoose an option:")
    for i, option in enumerate(choices, start=1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def adventure_game():
    introduction()

    # First choice
    choices = ["Go left", "Go right"]
    choice = make_choice(choices)

    if choice == 1:
        print("\nYou chose to go left.")
        time.sleep(1)
        print("You encounter a mystical forest.")
        time.sleep(1)
        print("A fairy offers you a magical potion. Do you accept?")
        choices = ["Yes", "No"]
        choice = make_choice(choices)

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
        choice = make_choice(choices)

        if choice == 1:
            print("\nYou open the chest and find a pile of gold coins.")
            time.sleep(1)
            print("Congratulations! You're rich!")
        else:
            print("\nYou decide not to open the chest and continue your journey.")

    print("\nThanks for playing the Simple Adventure Game!")

if __name__ == "__main__":
    adventure_game()