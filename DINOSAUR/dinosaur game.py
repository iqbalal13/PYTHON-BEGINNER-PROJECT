import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
GROUND_HEIGHT = 50
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player variables
player_width, player_height = 50, 50
player_x = 100
player_y = HEIGHT - GROUND_HEIGHT - player_height
player_velocity_y = 0
jumping = False

# Obstacle variables
obstacle_width, obstacle_height = 30, 30
obstacle_x = WIDTH
obstacle_y = HEIGHT - GROUND_HEIGHT - obstacle_height

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dinosaur Game")
clock = pygame.time.Clock()

# Functions
def draw_player():
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

def draw_obstacle():
    pygame.draw.rect(screen, WHITE, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not jumping:
        jumping = True
        player_velocity_y = -15  # Jump velocity

    # Update player position
    player_y += player_velocity_y

    # Gravity
    if player_y < HEIGHT - GROUND_HEIGHT - player_height:
        player_velocity_y += 1
    else:
        player_y = HEIGHT - GROUND_HEIGHT - player_height
        player_velocity_y = 0
        jumping = False

    # Update obstacle position
    obstacle_x -= 5

    # Check for collision with obstacle
    if (
        player_x < obstacle_x + obstacle_width
        and player_x + player_width > obstacle_x
        and player_y < obstacle_y + obstacle_height
        and player_y + player_height > obstacle_y
    ):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Respawn obstacle if it goes off the screen
    if obstacle_x + obstacle_width < 0:
        obstacle_x = WIDTH
        obstacle_y = HEIGHT - GROUND_HEIGHT - obstacle_height

    # Draw everything
    screen.fill(BLACK)
    draw_player()
    draw_obstacle()
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()