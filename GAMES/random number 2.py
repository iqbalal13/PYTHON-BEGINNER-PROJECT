import random

secret_number = random.randint(1, 20)

print("I'm thinking of a number between 1 and 100. Can you guess it?")

for guess_count in range(1, 10):
    guess = int(input(f"Guess #{guess_count}: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    elif guess == secret_number:
        print(f"You are right !, and you guessed it in {guess_count} times attempt")
        quit()
    elif guess == str():
        print(f"input harus angka ! {guess_count} times attempt")
        quit()
    else:
        print("input salah !")
        break
else:
    print(f"Sorry, you ran out of guesses. The number was {secret_number}.")