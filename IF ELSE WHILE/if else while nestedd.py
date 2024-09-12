print("Welcome to the car simulator!")

current_step = "start"

while True:
    if current_step == "start":
        step = input("You are at the 'start' step. Enter 'drive' to proceed: ")
        if step == "drive":
            current_step = "drive"
        else:
            print("Invalid step. You must enter 'drive' to proceed.")
    elif current_step == "drive":
        step = input("You are at the 'drive' step. Enter 'stop' to complete your journey: ")
        if step == "stop":
            print("Car stopped. You've completed your journey.")
            break
        else:
            print("Invalid step. You must enter 'stop' to complete your journey.")
    else:
        break