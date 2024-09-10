import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 10

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pinball Game")

# Create the ball
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [2, 2]

# Create the paddle
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# Game loop
game_running = True
while game_running:
    # Handle events
    event = pygame.event.poll()
    while event.type != pygame.NOEVENT:
        if event.type == pygame.QUIT:
            game_running = False
        event = pygame.event.poll()

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(5, 0)

    # Update the ball position
    ball.move_ip(ball_speed)

    # Check for collisions with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]
    if ball.top <= 0:
        ball_speed[1] = -ball_speed[1]

    # Check for collisions with the paddle
    if ball.colliderect(paddle):
        ball_speed[1] = -ball_speed[1]

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.ellipse(screen, RED, ball)
    pygame.draw.rect(screen, RED, paddle)
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()