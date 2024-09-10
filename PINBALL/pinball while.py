import random

class PinballMachine:
    def __init__(self):
        self.score = 0

    def play(self):
        try:
            hit_target = random.choice([True, False])

            if hit_target:
                self.score += 10
                print("Target hit! +10 points")
            else:
                raise ValueError("Ball missed the target!")

        except ValueError as e:
            print(f"Error: {e}")
            print("Ball lost! Try again.")

    def display_score(self):
        print(f"Current score: {self.score}")

# Main game loop
pinball_machine = PinballMachine()

while True:
    pinball_machine.play()
    pinball_machine.display_score()

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != 'yes':
        print("Thanks for playing! Final score:", pinball_machine.score)
        break
    else:
        print("-" * 20)