import random

print("Welcome to the Number Guessing Game!")
print("You have to guess a number between 1 to 10.")

MAX_GUESSES = 10
player_score = 0

for num_guesses in range(MAX_GUESSES):
    player_guess = int(input("Enter your guess: "))
    computer_guess = random.randint(1, 10)

    if player_guess == computer_guess:
        print("Congratulations! You win!")
        player_score += 1
        break
    else:
        print("Oops! Computer wins.")

print(f"Your final score is {player_score}/{num_guesses+1}. Thank you for playing!")