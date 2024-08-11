import random

print("Welcome to the Number Guessing Game!")
print("You have to guess a number between 1 to 10.")

for i in range(10):
    player_guess = int(input("Enter your guess: "))
    computer_guess = random.randint(1, 10)

    if player_guess == computer_guess:
        print("Congratulations! You win!")
        break
    else:
        print("Oops! Computer wins.")

print("Thank you for playing!")