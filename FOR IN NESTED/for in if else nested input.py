count = int(input("Enter the number of iterations: "))

for i in range(1, count + 1):
    user_input = input(f"Enter a value for iteration {i}: ")
    
    if user_input == "yes":
        print("You chose 'yes' for this iteration.")
    else:
        print("You did not choose 'yes' for this iteration.")