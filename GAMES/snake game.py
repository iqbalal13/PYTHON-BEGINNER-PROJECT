import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Snake
snake_block = 10
snake_speed = 15

# Clock to control the speed of the game
clock = pygame.time.Clock()

# Font for displaying the score
font = pygame.font.SysFont(None, 35)

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(window, white, [x[0], x[1], snake_block, snake_block])

# Function to display the score
def Your_score(score):
    value = font.render("Your Score: " + str(score), True, white)
    window.blit(value, [0, 0])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the snake
    x1, y1 = width / 2, height / 2

    # Initial movement direction
    x1_change, y1_change = 0, 0

    # Initial length of the snake
    snake_list = []
    length_of_snake = 1

    # Initial position of the food
    foodx, foody = round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            window.fill(black)
            Your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Check if the snake hits the boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        # Update the position of the food and increase the length of the snake when it eats the food
        if x1 == foodx and y1 == foody:
            foodx, foody = round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Update the display
        window.fill(black)
        pygame.draw.rect(window, red, [foodx, foody, snake_block, snake_block])
        our_snake(snake_block, snake_list)

        # Check if the snake collides with itself
        for segment in snake_list:
            if segment == [x1, y1]:
                game_close = True

        # Update the length of the snake
        if len(snake_list) >= length_of_snake:
            del snake_list[0]

        # Add the new head of the snake
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        # Draw the snake
        our_snake(snake_block, snake_list)

        # Update the display
        pygame.display.update()

        # Set the speed of the game
        clock.tick(snake_speed)

    # Quit Pygame
    pygame.quit()
    # Quit the program
    sys.exit()

# Start the game loop
gameLoop()