import time

def print_welcome_message():
    print("Welcome to the Simple Adventure Game!")
    time.sleep(1)
    print("You find yourself standing at a crossroad.")
    time.sleep(1)
    print("Make a choice to determine your destiny.")

def make_choice(choices, max_attempts):
    for attempts in range(max_attempts):
        user_input = input(f"\nChoose an option:\n1. {choices[0]}\n2. {choices[1]}\nEnter the number of your choice: ")

        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Please enter a valid number.")
        else:
            print("Invalid input. Please enter a number.")

    print("Too many invalid attempts. Exiting.")
    exit()

def play_left_path():
    print("\nYou chose to go left.")
    time.sleep(1)
    print("You encounter a mystical forest.")
    time.sleep(1)
    print("A fairy offers you a magical potion. Do you accept?")

    choices = ["Yes", "No"]
    choice = make_choice(choices, 3)

    if choice == 1:
        print("\nYou accept the potion and feel a surge of magical energy.")
        time.sleep(1)
        print("The fairy guides you safely through the forest.")
    else:
        print("\nYou decline the potion and cautiously navigate the forest.")
        time.sleep(1)
        print("You emerge safely on the other side.")
        return 1  # Additional point for making it through the forest

def play_right_path():
    print("\nYou chose to go right.")
    time.sleep(1)
    print("You find a treasure chest.")
    time.sleep(1)
    print("Do you open the chest?")

    choices = ["Yes", "No"]
    choice = make_choice(choices, 3)

    if choice == 1:
        print("\nYou open the chest and find a pile of gold coins.")
        time.sleep(1)
        print("Congratulations! You're rich!")
        return 2  # Additional points for finding the treasure
    else:
        print("\nYou decide not to open the chest and continue your journey.")
        return 0

def main():
    print_welcome_message()

    # First choice
    choices = ["Go left", "Go right"]
    choice = make_choice(choices, 3)

    score = 0

    if choice == 1:
        score += play_left_path()
    else:
        score += play_right_path()

    print(f"\nThanks for playing the Simple Adventure Game!\nYour final score: {score}")

if __name__ == "__main__":
    main()