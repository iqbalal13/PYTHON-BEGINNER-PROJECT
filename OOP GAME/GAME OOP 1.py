import random


class GuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.guesses = 0

    def play(self):
        print("Guess a number between 1 and 100.")
        while True:
            guess = int(input())
            self.guesses += 1

            if guess < self.number:
                print("Too low. Guess again.")
            elif guess > self.number:
                print("Too high. Guess again.")
            else:
                print(f"Congratulations! You guessed the number in {self.guesses} guesses.")
                break


game = GuessingGame()
game.play()