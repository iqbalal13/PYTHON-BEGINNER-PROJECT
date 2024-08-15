import random

class GameBot:
    def __init__(self):
        self.secret_number = None
        self.score = 0

    def start_game(self):
        print("Welcome to the Guessing Game!")
        self.secret_number = random.randint(1, 100)
        attempts = 0

        for outer_attempts in range(3):  # Limit the number of attempts to 3 for this example
            inner_attempts = 0
            while inner_attempts < 3:  # Limit the number of input attempts to 3 for this example
                user_input = input("Enter your guess (1-100), 'skip' to pass the question: ")

                if user_input.lower() == 'skip':
                    print("Question skipped. Your score for this question is set to 0.")
                    self.score = 0
                    break
                elif user_input.isdigit():
                    guess = int(user_input)
                    if 1 <= guess <= 100:
                        break
                    else:
                        print("Please enter a number between 1 and 100.")
                else:
                    print("Invalid input. Please enter a valid number or 'skip'.")
                
                inner_attempts += 1

            if inner_attempts == 3:
                print("Too many invalid inputs. Game over.")
                break

            attempts += 1

            if guess == self.secret_number:
                print(f"Congratulations! You guessed the correct number {self.secret_number} in {attempts} attempts.")
                self.score += 1
            else:
                print(f"Wrong guess. The correct number is {self.secret_number}. Your score for this question is decreased by 1.")
                self.score -= 1

            print(f"Your current score: {self.score}")
            outer_attempts += 1

if __name__ == "__main__":
    bot = GameBot()
    bot.start_game()