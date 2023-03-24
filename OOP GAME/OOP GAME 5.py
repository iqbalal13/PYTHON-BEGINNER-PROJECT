import random


class NumberGame:
    def __init__(self):
        self.target_number = random.randint(1, 100)
        self.num_guesses = 0
        self.max_guesses = 5

    def guess(self, num):
        self.num_guesses += 1

        if num == self.target_number:
            return "Congratulations! You guessed the number in {} guesses.".format(self.num_guesses)
        elif num > self.target_number:
            return "The number is lower than {}".format(num)
        else:
            return "The number is higher than {}".format(num)

        if self.num_guesses >= self.max_guesses:
            return "You've reached the maximum number of guesses. The number was {}.".format(self.target_number)


def main():
    game = NumberGame()
    print("Guess the number between 1 and 100. You have {} guesses.".format(game.max_guesses))

    for i in range(game.max_guesses):
        while True:
            guess = input("Enter your guess: ")
            try:
                guess = int(guess)
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        result = game.guess(guess)
        print(result)

        if "Congratulations" in result or "maximum number of guesses" in result:
            break

    print("Game over.")


if __name__ == "__main__":
    main()