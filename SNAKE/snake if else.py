import random
import os
import time

def print_board(snake, fruit, board_size):
    os.system("cls" if os.name == "nt" else "clear")
    i, j = divmod(fruit[0] * board_size + fruit[1], board_size)
    for x in range(board_size):
        for y in range(board_size):
            print("F" if (x, y) == fruit else "S" if (x, y) in snake else ".", end=" ")
        print()

def move(snake, direction):
    head = snake[-1]
    i, j = head
    if direction == "UP":
        new_head = (i - 1, j)
    elif direction == "DOWN":
        new_head = (i + 1, j)
    elif direction == "LEFT":
        new_head = (i, j - 1)
    elif direction == "RIGHT":
        new_head = (i, j + 1)
    return new_head

def snake_game(snake, direction, fruit, board_size):
    print_board(snake, fruit, board_size)
    print("Use W, A, S, D to control the snake. Q to quit.")

    user_input = input("Enter your move: ").upper()

    if user_input == "Q":
        return

    if user_input in ("W", "A", "S", "D"):
        direction = "UP" if user_input == "W" else direction
        direction = "LEFT" if user_input == "A" else direction
        direction = "DOWN" if user_input == "S" else direction
        direction = "RIGHT" if user_input == "D" else direction

        new_head = move(snake, direction)

        if (
            0 <= new_head[0] < board_size
            and 0 <= new_head[1] < board_size
            and new_head not in snake
        ):
            snake.append(new_head)
            if new_head == fruit:
                fruit = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
        else:
            print("Game Over!")
            return

    else:
        print("Invalid input. Use W, A, S, D to control the snake. Q to quit.")
        return

    time.sleep(0.5)
    snake_game(snake, direction, fruit, board_size)

if __name__ == "__main__":
    initial_snake = [(0, 0)]
    initial_direction = "RIGHT"
    initial_fruit = (random.randint(0, 9), random.randint(0, 9))
    board_size = 10
    snake_game(initial_snake, initial_direction, initial_fruit, board_size)