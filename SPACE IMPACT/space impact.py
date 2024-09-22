import random
import time
import os

# Define player
class Player:
    def __init__(self):
        self.health = 100
        self.score = 0

# Define enemy
class Enemy:
    def __init__(self, position):
        self.position = position
        self.health = 10

# Game setup
player = Player()
enemies = []

# Game functions
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_enemies():
    for i in range(5):
        position = random.randint(1, 50)
        enemies.append(Enemy(position))

def display_game():
    print(f"Health: {player.health} | Score: {player.score}")
    print("@" * 50)
    game_map = [' '] * 50
    for enemy in enemies:
        game_map[enemy.position - 1] = 'X'
    print(''.join(game_map))

def move_enemies():
    for enemy in enemies:
        enemy.position -= 1
        if enemy.position == 0:
            player.health -= 10
            enemies.remove(enemy)

def shoot():
    global player
    if 'X' in ''.join([' ' if enemy.position != 1 else 'X' for enemy in enemies]):
        player.score += 10
        enemies.pop(0)

# Game loop
generate_enemies()
while player.health > 0:
    clear_screen()
    display_game()
    move_enemies()
    action = input("Press 's' to shoot: ").lower()
    if action == 's':
        shoot()
    time.sleep(0.5)

print("Game Over!")
print(f"Your final score is: {player.score}")