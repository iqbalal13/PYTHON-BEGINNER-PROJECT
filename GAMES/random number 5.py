import random

print("Welcome to the Number Guessing Game!")
print("You have to guess a number between 1 to 10.")

player_guess = int(input("Enter your guess: "))
computer_guess = random.randint(1, 10)

while True:
    if player_guess == computer_guess:
        print("Congratulations! You win!")
        break
    else:
        print("Oops! Computer wins.")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == 'y':
            player_guess = int(input("Enter your guess: "))
            computer_guess = random.randint(1, 10)
        else:
            print("Thank you for playing!")
            break