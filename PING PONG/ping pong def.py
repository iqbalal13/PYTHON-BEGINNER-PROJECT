import os
import time

def display_game(paddle_x, ball_x, ball_y, score):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
    print("**********")
    for i in range(8):
        print("*        *")
    print(f"Score: {score}")
    print("----------")
    print(" " * (paddle_x - 1) + "|P|" + " " * (10 - paddle_x))
    print(" " * ball_x + "O")

def move_paddle(paddle_x, move):
    if move == 'a' and paddle_x > 1:
        paddle_x -= 1
    elif move == 'd' and paddle_x < 18:
        paddle_x += 1
    return paddle_x

def update_ball_position(ball_x, ball_y, ball_vx, ball_vy, paddle_x, score):
    ball_y += ball_vy
    ball_x += ball_vx

    # Ball bouncing off walls
    if ball_y == 0 or ball_y == 9:
        ball_vy = -ball_vy

    # Ball bouncing off paddle
    if ball_y == 8 and paddle_x - 1 <= ball_x <= paddle_x + 1:
        ball_vy = -ball_vy
        score += 1  # Increase score when the ball bounces off the paddle

    # Ball bouncing off the left or right wall
    if ball_x == 0 or ball_x == 19:
        ball_vx = -ball_vx

    return ball_x, ball_y, ball_vx, ball_vy, score

def main():
    ball_y, ball_x = 5, 10
    ball_vy, ball_vx = 1, 1
    paddle_x = 9
    score = 0

    while True:
        display_game(paddle_x, ball_x, ball_y, score)

        # Move paddle based on user input
        move = input("Move paddle (a/d): ")

        try:
            paddle_x = move_paddle(paddle_x, move)
        except ValueError as e:
            print(f"Error: {e}")
            continue

        ball_x, ball_y, ball_vx, ball_vy, score = update_ball_position(
            ball_x, ball_y, ball_vx, ball_vy, paddle_x, score
        )

        # Check for game over
        if ball_y == 9:
            print("Game Over!")
            time.sleep(2)
            break
        time.sleep(0.1)  # Pause to make the game viewable

if __name__ == "__main__":
    main()