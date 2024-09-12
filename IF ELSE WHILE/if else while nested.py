print("Welcome to the car simulator!")

while True:
    step = input("Enter the step (start, drive, stop): ")

    if step == "start":
        print("Car started. You can now drive the car.")
        drive = input("Do you want to drive the car? (yes/no): ")
        if drive == "yes":
            print("Car is moving. Drive safely!")
        else:
            print("Car remains stationary.")
    elif step == "drive":
        print("Car is already moving. Drive safely!")
    elif step == "stop":
        print("Car stopped. You've completed your journey.")
        break
    else:
        print("Invalid step. Please enter 'start', 'drive', or 'stop'.")