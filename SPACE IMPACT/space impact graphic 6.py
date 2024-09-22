import pygame
import random
import time
import sys

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Impact")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load images
player_image = pygame.image.load("player.png")
enemy_image = pygame.image.load("enemy.png")

# Define player
class Player:
    def __init__(self):
        self.health = 100
        self.score = 0
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (50, SCREEN_HEIGHT // 2)

# Define enemy
class Enemy:
    def __init__(self, position, speed):
        self.health = 10
        self.speed = speed
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.center = (position, random.randint(50, SCREEN_HEIGHT - 50))

# Function to reset game
def reset_game():
    global player, enemies, start_time, game_duration
    player = Player()
    enemies = []
    generate_enemies()
    start_time = time.time()

# Function to select difficulty
def select_difficulty():
    while True:
        print("Select Difficulty:")
        print("1. Easy")
        print("2. Hard")
        choice = input("Enter your choice (1/2): ")
        if choice == '1':
            return 5, 60  # 5 enemies, 60 seconds duration
        elif choice == '2':
            return 10, 45  # 10 enemies, 45 seconds duration
        else:
            print("Invalid choice! Please enter 1 or 2.")

# Game setup
player = Player()
enemies = []
num_enemies, game_duration = select_difficulty()
generate_enemies()
start_time = time.time()

# Game functions
def generate_enemies():
    for i in range(num_enemies):
        position = random.randint(SCREEN_WIDTH + 100, SCREEN_WIDTH + 400)
        speed = random.randint(3, 6)  # random speed between 3 and 6
        enemies.append(Enemy(position, speed))

def move_enemies():
    for enemy in enemies:
        enemy.rect.x -= enemy.speed
        if enemy.rect.right < 0:
            player.health -= 10
            enemies.remove(enemy)

def shoot():
    global player
    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            player.score += 10
            enemies.remove(enemy)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        shoot()
    elif keys[pygame.K_q]:
        print("Quitting the game...")
        pygame.quit()
        sys.exit()

    move_enemies()

    screen.fill(WHITE)
    screen.blit(player.image, player.rect)
    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect)

    pygame.display.flip()

    if player.health <= 0 or time.time() - start_time >= game_duration:
        print("Game Over! Time's up!")
        print(f"Your final score is: {player.score}")
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice == 'y':
            num_enemies, game_duration = select_difficulty()
            reset_game()
        else:
            running = False

    if player.score >= 50:
        print("You Win!")
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice == 'y':
            num_enemies, game_duration = select_difficulty()
            reset_game()
        else:
            running = False

    clock.tick(30)

pygame.quit()