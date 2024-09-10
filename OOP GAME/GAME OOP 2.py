import random


class GuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guesses = 0

    def play(self):
        print("Guess a number between 1 and 100.")
        guess = int(input())

        while guess != self.number:
            self.guesses += 1

            if guess < self.number:
                print("Too low. Guess again.")
            elif guess > self.number:
                print("Too high. Guess again.")

            guess = int(input())

        self.guesses += 1
        print(f"Congratulations! You guessed the number in {self.guesses} guesses.")


game = GuessingGame()
game.play()