import random

class PinballMachine:
    def __init__(self):
        self.score = 0

    def play(self):
        try:
            # Simulate a ball hitting a bumper or target
            hit_target = random.choice([True, False])

            if hit_target:
                self.score += 10
                print("Target hit! +10 points")
            else:
                # Simulate a ball missing the target and causing an error
                raise ValueError("Ball missed the target!")

        except ValueError as e:
            print(f"Error: {e}")
            print("Ball lost! Try again.")

    def display_score(self):
        print(f"Current score: {self.score}")

# Example usage
pinball_machine = PinballMachine()

for _ in range(5):
    pinball_machine.play()
    pinball_machine.display_score()
    print("-" * 20)