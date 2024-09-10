import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BRICK_WIDTH, BRICK_HEIGHT = 80, 30
FPS = 60
WHITE = (255, 255, 255)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pinball Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Ball properties
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed_x, ball_speed_y = random.choice([-5, 5]), -5

# Paddle properties
paddle_x = (WIDTH - PADDLE_WIDTH) // 2
paddle_y = HEIGHT - PADDLE_HEIGHT - 20
paddle_speed = 0

# Bricks
bricks = []
for row in range(3):
    for col in range(WIDTH // BRICK_WIDTH):
        brick = pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Score
score = 0

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speed = -10
            elif event.key == pygame.K_RIGHT:
                paddle_speed = 10
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                paddle_speed = 0

    # Move paddle
    paddle_x += paddle_speed
    if paddle_x < 0:
        paddle_x = 0
    elif paddle_x > WIDTH - PADDLE_WIDTH:
        paddle_x = WIDTH - PADDLE_WIDTH

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball bouncing off walls
    if ball_x - BALL_RADIUS < 0 or ball_x + BALL_RADIUS > WIDTH:
        ball_speed_x = -ball_speed_x
    if ball_y - BALL_RADIUS < 0:
        ball_speed_y = -ball_speed_y

    # Ball bouncing off paddle
    if (
        paddle_x < ball_x < paddle_x + PADDLE_WIDTH
        and paddle_y < ball_y < paddle_y + PADDLE_HEIGHT
    ):
        ball_speed_y = -ball_speed_y

    # Check for collisions with bricks
    for brick in bricks[:]:
        if brick.colliderect((ball_x - BALL_RADIUS, ball_y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)):
            ball_speed_y = -ball_speed_y
            bricks.remove(brick)
            score += 10

    # Check for game over
    if ball_y > HEIGHT:
        score = 0
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2

    # Draw everything
    screen.fill((0, 0, 0))

    # Draw bricks
    for brick in bricks:
        pygame.draw.rect(screen, WHITE, brick)

    # Draw paddle
    pygame.draw.rect(screen, WHITE, (paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Draw ball
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)