import random

print("Welcome to the Number Guessing Game!")
print("You have to guess a number between 1 to 10.")

MAX_GUESSES = 10
num_guesses = 0
player_score = 0

while num_guesses < MAX_GUESSES:
    player_guess = int(input("Enter your guess: "))
    computer_guess = random.randint(1, 10)
    if player_guess == computer_guess:
        print("Congratulations! You win!")
        player_score += 1
    elif player_guess > computer_guess:
        print("terlalu besar")
        num_guesses += 1
    elif player_guess < computer_guess:
        print("terlalu kecil")
        num_guesses += 1
    else:
        print("Input salah.")
if num_guesses > player_score:
    print("you lose")
elif num_guesses < player_score:
    print("you win")
elif num_guesses == player_score:
    print("hasil seri !!")
elif num_guesses == MAX_GUESSES:
    print("Sorry, you didn't guess the number in time. Game over.")

print(f"Your final score is {player_score}/{MAX_GUESSES}. Thank you for playing! ")