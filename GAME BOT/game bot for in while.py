import random

class GameBot:
    def __init__(self):
        self.secret_number = None

    def start_game(self):
        print("Welcome to the Guessing Game!")
        self.secret_number = random.randint(1, 100)
        self.play_game()

    def play_game(self):
        attempts = 0

        for _ in range(3):  # Limit the number of attempts to 3 for this example
            guess = self.get_user_guess()
            attempts += 1

            if guess == self.secret_number:
                print(f"Congratulations! You guessed the correct number {self.secret_number} in {attempts} attempts.")
                break
            elif guess < self.secret_number:
                print("Too low. Try again!")
            else:
                print("Too high. Try again!")

    def get_user_guess(self):
        while True:
            try:
                guess = int(input("Enter your guess (1-100): "))
                if 1 <= guess <= 100:
                    return guess
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    bot = GameBot()
    bot.start_game()