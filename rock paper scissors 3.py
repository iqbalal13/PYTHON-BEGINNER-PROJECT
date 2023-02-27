import random

computer_score = 0
player_score = 0
print("Welcome to the rock-paper-scissors game!")

for rounds_played in range(3):  # repeat the game three times
    print("Round", rounds_played + 1)
    print("Choose your weapon:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    player_choice = int(input("Enter your choice (1-3): "))

    computer_choices = {1: "rock", 2: "paper", 3: "scissors"}
    computer_choice = random.randint(1, 3)

    print("You chose:", computer_choices[player_choice])
    print("The computer chose:", computer_choices[computer_choice])

    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == 1 and computer_choice == 3:
        print("You win! Rock beats scissors.")
        player_score += 1
    elif player_choice == 2 and computer_choice == 1:
        print("You win! Paper beats rock.")
        player_score += 1
    elif player_choice == 3 and computer_choice == 2:
        print("You win! Scissors beats paper.")
        player_score += 1
    else:
        print("The computer wins!")
        computer_score += 1

print("Final score:")
print("Player:", player_score)
print("Computer:", computer_score)