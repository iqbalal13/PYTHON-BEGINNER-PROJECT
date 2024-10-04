import os
import time

ball_y, ball_x = 5, 10
ball_vy, ball_vx = 1, 1
paddle_x = 9
score = 0

os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen

# Display initial game state
print("**********")
for i in range(8):
    print("*        *")
print("----------")
print(f"Score: {score}")

# Move ball
ball_y += ball_vy
ball_x += ball_vx

# Move paddle based on user input
move = input("Move paddle (a/d): ")
if move == 'a' and paddle_x > 1:
    paddle_x -= 1
elif move == 'd' and paddle_x < 18:
    paddle_x += 1

# Ball bouncing off walls
if ball_y == 0 or ball_y == 9:
    ball_vy = -ball_vy
if ball_x == 0 or ball_x == 19:
    ball_vx = -ball_vx

# Ball bouncing off paddle
if ball_y == 8 and paddle_x - 1 <= ball_x <= paddle_x + 1:
    ball_vy = -ball_vy
    score += 1

# Display updated game state
os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
print("**********")
for i in range(8):
    print("*        *")
print("----------")
print(f"Score: {score}")

# Check for game over
if ball_y == 9:
    print("Game Over!")
    time.sleep(2)