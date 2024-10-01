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
        lives -= 1
        print(f"Missed! Lives left: {lives}")

    # Update paddle position based on user input
    user_input = input("Move paddle left (L) or right (R): ")
    if user_input == "L":
        paddle_position -= 1
    elif user_input == "R":
        paddle_position += 1
    else:
        print("Invalid input. Try again.")

# Game over
print("Game over! Your final score:", score)