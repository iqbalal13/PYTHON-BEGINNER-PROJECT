import random

# Pinball variables
ball_position = 0
paddle_position = 0
score = 0
lives = 3

# Main game loop
while lives > 0:
    # Simulate ball movement
    ball_position += random.randint(-1, 1)

    # Check if ball hit the paddle
    if ball_position == paddle_position:
        score += 1
        print(f"Score: {score}")
    else:
        try:
            # Attempt to get user input
            user_input = input("Move paddle left (L) or right (R): ")

            # Handle user input
            if user_input == "L":
                paddle_position -= 1
            elif user_input == "R":
                paddle_position += 1
            else:
                raise ValueError("Invalid input. Please enter 'L' or 'R'.")
        except ValueError as e:
            print(f"Error: {e}")
            continue

        lives -= 1
        print(f"Missed! Lives left: {lives}")

# Game over
print("Game over! Your final score:", score)