import random
import time
import os
import sys


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


def display_interface():
    print("+" + "-" * 30 + "+")
    print("| Health: {:<4} | Score: {:<4} |".format(player.health, player.score))
    print("+" + "-" * 30 + "+")
    print("Instructions:")
    print("'s' - Shoot")
    print("'q' - Quit")
    print("+" + "-" * 30 + "+")


def display_game():
    print(" " * 50 + "|")
    for enemy in enemies:
        print(" " * (enemy.position - 1) + "X", end='')
    print()


def move_enemies():
    for enemy in enemies:
        enemy.position -= 1
        if enemy.position == 0:
            player.health -= 10
            enemies.remove(enemy)


def shoot():
    global player
    for enemy in enemies:
        if enemy.position == 1:
            player.score += 10
            enemies.remove(enemy)


# Game loop
generate_enemies()
while player.health > 0:
    clear_screen()
    display_interface()
    display_game()
    move_enemies()
    action = input("Enter your action: ").lower()
    if action == 's':
        shoot()
    elif action == 'q':
        print("Quitting the game...")
        sys.exit()

    if player.score >= 50:
        print("You Win!")
        break

    time.sleep(0.5)

if player.health <= 0:
    print("Game Over! You Lose!")
    print(f"Your final score is: {player.score}")