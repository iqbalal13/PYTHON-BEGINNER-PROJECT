import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
BALL_RADIUS = 10
WHITE = (255, 255, 255)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Ping Pong")

# Initialize clock
clock = pygame.time.Clock()

# Initialize game variables
ball_position = [WIDTH // 2, HEIGHT // 2]
ball_speed = [5, 5]

paddle_a_position = [10, HEIGHT // 2 - PADDLE_HEIGHT // 2]
paddle_b_position = [WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2]
paddle_speed = 5

score_a = 0
score_b = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a_position[1] > 0:
        paddle_a_position[1] -= paddle_speed
    if keys[pygame.K_s] and paddle_a_position[1] < HEIGHT - PADDLE_HEIGHT:
        paddle_a_position[1] += paddle_speed

    if keys[pygame.K_UP] and paddle_b_position[1] > 0:
        paddle_b_position[1] -= paddle_speed
    if keys[pygame.K_DOWN] and paddle_b_position[1] < HEIGHT - PADDLE_HEIGHT:
        paddle_b_position[1] += paddle_speed

    # Update ball position
    ball_position[0] += ball_speed[0]
    ball_position[1] += ball_speed[1]

    # Check collision with walls
    if ball_position[0] <= 0:
        ball_speed[0] = abs(ball_speed[0])
        score_b += 1
    elif ball_position[0] >= WIDTH:
        ball_speed[0] = -abs(ball_speed[0])
        score_a += 1

    if ball_position[1] <= 0 or ball_position[1] >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Check collision with paddles
    if (
        paddle_a_position[0] <= ball_position[0] <= paddle_a_position[0] + PADDLE_WIDTH
        and paddle_a_position[1] <= ball_position[1] <= paddle_a_position[1] + PADDLE_HEIGHT
    ) or (
        paddle_b_position[0] <= ball_position[0] <= paddle_b_position[0] + PADDLE_WIDTH
        and paddle_b_position[1] <= ball_position[1] <= paddle_b_position[1] + PADDLE_HEIGHT
    ):
        ball_speed[0] = -ball_speed[0]

    # Draw everything
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, WHITE, (int(ball_position[0]), int(ball_position[1])), BALL_RADIUS)
    pygame.draw.rect(screen, WHITE, (paddle_a_position[0], paddle_a_position[1], PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (paddle_b_position[0], paddle_b_position[1], PADDLE_WIDTH, PADDLE_HEIGHT))

    # Display scores
    font = pygame.font.Font(None, 36)
    score_text_a = font.render(f"Player A: {score_a}", True, WHITE)
    score_text_b = font.render(f"Player B: {score_b}", True, WHITE)
    screen.blit(score_text_a, (10, 10))
    screen.blit(score_text_b, (WIDTH - 200, 10))

    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)