import pygame
import time
import random

pygame.init()

# Set up the display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake and Apple sizes
block_size = 20
snake_speed = 15

font = pygame.font.SysFont(None, 35)

# Function to draw the snake
def snake(snake_list):
    index = 0
    while index < len(snake_list):
        segment = snake_list[index]
        pygame.draw.rect(display, green, [segment[0], segment[1], block_size, block_size])
        index += 1

# Function to display the score
def your_score(score):
    score_text = font.render("Your Score: " + str(score), True, white)
    display.blit(score_text, [0, 0])

# The main game function
def gameLoop():
    game_over = False
    game_close = False

    # Initial snake position and direction
    lead_x = width / 2
    lead_y = height / 2
    lead_x_change = 0
    lead_y_change = 0

    # Initial snake length
    snake_list = []
    length_of_snake = 1

    # Initial apple position
    apple_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
    apple_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0

    while not game_over:

        while game_close:
            display.fill(black)
            your_score(length_of_snake - 1)
            pygame.display.update()

            events = pygame.event.get()
            try:
                for event in events:
                    if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        elif event.key == pygame.K_c:
                            gameLoop()
            except pygame.error as e:
                print("Error: ", e)

        events = pygame.event.get()
        try:
            for event in events:
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        lead_x_change = -block_size
                        lead_y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        lead_x_change = block_size
                        lead_y_change = 0
                    elif event.key == pygame.K_UP:
                        lead_y_change = -block_size
                        lead_x_change = 0
                    elif event.key == pygame.K_DOWN:
                        lead_y_change = block_size
                        lead_x_change = 0
        except pygame.error as e:
            print("Error: ", e)

        # Check if the snake hits the boundaries
        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            game_close = True

        # Update snake position
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Draw the background
        display.fill(black)

        # Draw the apple
        pygame.draw.rect(display, red, [apple_x, apple_y, block_size, block_size])

        # Draw the snake
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Check if the snake hits itself
        index = 0
        while index < len(snake_list) - 1:
            segment = snake_list[index]
            if segment == snake_head:
                game_close = True
            index += 1

        # Update the display
        snake(snake_list)
        your_score(length_of_snake - 1)
        pygame.display.update()

        # Check if the snake eats the apple
        if lead_x == apple_x and lead_y == apple_y:
            apple_x = round(random.randrange(0, width - block_size) / 20.0) * 20.0
            apple_y = round(random.randrange(0, height - block_size) / 20.0) * 20.0
            length_of_snake += 1

        # Set the snake speed
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

# Run the game