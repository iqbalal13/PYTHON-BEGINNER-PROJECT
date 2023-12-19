import time

def introduction():
    print("Welcome to the Adventure Game!")
    time.sleep(1)
    print("You find yourself in a dark cave.")
    time.sleep(1)
    print("You can see two paths ahead of you.")

def make_choice():
    print("\nWhat will you do?")
    print("1. Take the left path.")
    print("2. Take the right path.")
    choice = input("Enter your choice (1 or 2): ")
    return choice

def left_path():
    print("\nYou chose the left path.")
    time.sleep(1)
    print("You encounter a friendly dragon!")
    time.sleep(1)
    print("The dragon gives you a bag of gold.")
    time.sleep(1)
    print("Congratulations! You've completed the adventure.")

def right_path():
    print("\nYou chose the right path.")
    time.sleep(1)
    print("You enter a dark room.")
    time.sleep(1)
    print("A mysterious figure appears.")
    time.sleep(1)
    print("The figure challenges you to a riddle.")
    time.sleep(1)
    
    answer = input("What has keys but can't open locks? ").lower()
    
    if answer == "piano":
        print("Correct! The figure rewards you.")
        print("Congratulations! You've completed the adventure.")
    else:
        print("Incorrect! The figure disappears, and the room starts to shake.")
        print("Oh no, the room is collapsing! Game over.")

def main():
    introduction()
    
    while True:
        choice = make_choice()
        
        if choice == "1":
            left_path()
            break
        elif choice == "2":
            right_path()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()