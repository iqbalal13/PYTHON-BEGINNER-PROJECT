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
    i = 0
    while i < 5:
        position = random.randint(1, 50)
        enemies.append(Enemy(position))
        i += 1


def display_game():
    print(f"Health: {player.health} | Score: {player.score}")
    print("@" * 50)
    game_map = [' '] * 50
    i = 0
    while i < len(enemies):
        game_map[enemies[i].position - 1] = 'X'
        i += 1
    print(''.join(game_map))


def move_enemies():
    i = 0
    while i < len(enemies):
        enemies[i].position -= 1
        if enemies[i].position == 0:
            player.health -= 10
            enemies.pop(i)
            i -= 1
        i += 1


def shoot():
    global player
    i = 0
    while i < len(enemies):
        if enemies[i].position == 1:
            player.score += 10
            enemies.pop(i)
            i -= 1
        i += 1


# Game loop
generate_enemies()
while player.health > 0:
    clear_screen()
    display_game()
    move_enemies()
    action = input("Press 's' to shoot: ").lower()
    if action == 's':
        shoot()

    if player.score >= 50:
        print("You Win!")
        break

    time.sleep(0.5)

if player.health <= 0:
    print("Game Over! You Lose!")
    print(f"Your final score is: {player.score}")