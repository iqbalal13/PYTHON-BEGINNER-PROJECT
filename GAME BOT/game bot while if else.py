import random

class GameBot:
    def __init__(self):
        self.secret_number = None

    def start_game(self):
        print("Welcome to the Guessing Game!")
        self.secret_number = random.randint(1, 100)
        attempts = 0

        for _ in range(3):  # Limit the number of attempts to 3 for this example
            attempts += 1

            for _ in range(3):  # Limit the number of input attempts to 3 for this example
                user_input = input("Enter your guess (1-100): ")

                if user_input.isdigit():
                    guess = int(user_input)
                    if 1 <= guess <= 100:
                        break
                    else:
                        print("Please enter a number between 1 and 100.")
                else:
                    print("Invalid input. Please enter a valid number.")

            if guess == self.secret_number:
                print(f"Congratulations! You guessed the correct number {self.secret_number} in {attempts} attempts.")
                break
            elif guess < self.secret_number:
                print("Too low. Try again!")
            else:
                print("Too high. Try again!")

if __name__ == "__main__":
    bot = GameBot()
    bot.start_game()