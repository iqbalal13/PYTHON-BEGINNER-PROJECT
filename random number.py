import random

secret_number = random.randint(1, 20)

print("I'm thinking of a number between 1 and 100. Can you guess it?")

for guess_count in range(1, 11):
    guess = int(input(f"Guess #{guess_count}: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations, you guessed it in {guess_count} tries!")
        break
else:
    print(f"Sorry, you ran out of guesses. The number was {secret_number}.")