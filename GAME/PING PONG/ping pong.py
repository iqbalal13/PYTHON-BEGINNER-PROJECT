import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Paddle
paddle_width, paddle_height = 15, 100
player_paddle = pygame.Rect(width - 20 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)
opponent_paddle = pygame.Rect(10, height // 2 - paddle_height // 2, paddle_width, paddle_height)
paddle_speed = 15

# Ball
ball_size = 15
ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)
ball_speed = [7 * random.choice((1, -1)), 7 * random.choice((1, -1))]

# Score
player_score = 0
opponent_score = 0
font = pygame.font.SysFont(None, 35)

# Function to reset the ball
def reset_ball():
    return pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and opponent_paddle.top > 0:
        opponent_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and opponent_paddle.bottom < height:
        opponent_paddle.y += paddle_speed

    player_paddle.y = ball.y  # Make the player's paddle follow the ball

    # Update ball position
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collision with top and bottom walls
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_speed[0] = -ball_speed[0]

    # Scoring
    if ball.left <= 0:
        player_score += 1
        ball = reset_ball()
    elif ball.right >= width:
        opponent_score += 1
        ball = reset_ball()

    # Drawing everything on the window
    window.fill(black)
    pygame.draw.rect(window, white, player_paddle)
    pygame.draw.rect(window, white, opponent_paddle)
    pygame.draw.ellipse(window, white, ball)
    pygame.draw.aaline(window, white, (width // 2, 0), (width // 2, height))

    # Display scores
    player_text = font.render(str(player_score), True, white)
    window.blit(player_text, (width // 2 + 20, 20))
    opponent_text = font.render(str(opponent_score), True, white)
    window.blit(opponent_text, (width // 2 - 40, 20))

    pygame.display.flip()

    pygame.time.Clock().tick(60)