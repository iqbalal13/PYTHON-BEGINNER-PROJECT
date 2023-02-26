import random

print("Welcome to the rock-paper-scissors game!")
print("Choose your weapon:")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

# Get the player's choice
player_choice = int(input("Enter your choice (1-3): "))

# Define the computer's choices
computer_choices = {1: "rock", 2: "paper", 3: "scissors"}

# Generate the computer's choice
computer_choice = random.randint(1, 3)

print("You chose:", computer_choices[player_choice])
print("The computer chose:", computer_choices[computer_choice])

# Determine the winner
if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == 1 and computer_choice == 3:
    print("You win! Rock beats scissors.")
elif player_choice == 2 and computer_choice == 1:
    print("You win! Paper beats rock.")
elif player_choice == 3 and computer_choice == 2:
    print("You win! Scissors beats paper.")
else:
    print("The computer wins!")