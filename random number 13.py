import random

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
    elif guess > secret_number:
        print("Too high!")
    elif guess == secret_number:
        print(f"You guessed the number in {guess_count} tries and your score is .")

else:
 print(f"Sorry, you ran out of guesses. The number was {secret_number}. Your score is .")