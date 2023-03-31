import random

rounds_played = 0
computer_score = 0
player_score = 0
print("Welcome to the rock-paper-scissors game!")

while rounds_played < 3:  # repeat the game until three rounds have been played
    rounds_played += 1
    print("Choose your weapon:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    player_choice = int(input("Enter your choice (1-3), or enter 0 to quit: "))

    if player_choice == 0:
        break  # exit the loop if the player chooses to quit

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

if player_score == computer_score:
    print("it's tie")
elif player_score > computer_score:
    print("player win")
elif player_score < computer_score:
    print("player win")
print("Final score:")
print("Player:", player_score)
print("Computer:", computer_score)