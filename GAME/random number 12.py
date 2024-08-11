import random

player_score = 0
computer_score = 0
secret_number = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20. Can you guess it?")
for guess_count in range(1, 10):
    guess = input(f"Guess #{guess_count}: ")
    if not guess.isdigit():
        print("Please enter a number!")
        continue
    guess = int(guess)
    if guess < secret_number:
        print("Too low!")
        computer_score += 1
    elif guess > secret_number:
        print("Too high!")
        computer_score += 11
    elif guess == secret_number:
        print("you're right")
        player_score += 1
if player_score > computer_score:
    print(f"you win You guessed the number in {guess_count}")
elif player_score < computer_score:
    print(f"you lose You guessed the number in {guess_count} tries and you're running out of guess")
elif player_score == computer_score:
    print(f"you lose You guessed the number in {guess_count} tries and you're running out of guess")
else:
 print("input salah")