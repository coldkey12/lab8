import pygame
import random

# Define colors
blue = (50, 153, 213)
black = (0, 0, 0)
white = (255, 255, 255)

# Screen dimensions and snake block size
dis_width = 600
dis_height = 400
snake_block = 10

# Initialize Pygame
pygame.init()

# Set up the display and clock
display = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()

# Load coin image
image = pygame.image.load("Coin.png")
image = pygame.transform.scale(image, (10, 10))

# Function to display the score and level
def display_score_and_level(score, level):
    font = pygame.font.SysFont("bahnschrift", 25)
    score_text = font.render("Score: " + str(score), True, white)
    level_text = font.render("Level: " + str(level), True, white)
    display.blit(score_text, [10, 10])  # Display score at the top left
    display.blit(level_text, [10, 40])  # Display level below score

# Main game function
def main():
    game_over = False
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Random food location
    food_x = random.randint(0, (dis_width - 20) // 10) * 10
    food_y = random.randint(0, (dis_height - 20) // 10) * 10

    # Initial snake movement changes (no movement at first)
    x1_change = 0
    y1_change = 0

    # Snake body list and initial length
    snake_list = []
    snake_length = 1

    # Score and level initialization
    score = 0
    level = 1
    speed = 15  # Initial speed

    # Game loop
    while not game_over:
        display.fill(blue)  # Fill the screen with blue

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

        # Update the snake's head position
        x1 += x1_change
        y1 += y1_change

        # Check if the snake eats the food
        if x1 == food_x and y1 == food_y:
            snake_length += 1  # Increase snake's length
            score += 1  # Increase score
            food_x = random.randint(0, (dis_width - 20) // 10) * 10  # Generate new food position
            food_y = random.randint(0, (dis_height - 20) // 10) * 10

            # Check if the player reaches the next level (every 3 foods eaten)
            if score % 3 == 0:
                level += 1  # Increase level
                speed += 3  # Increase speed (adjust this value for faster/slower speed increase)

        # Check for collision with the screen borders (game over if the snake hits the wall)
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        # Add the new head to the snake list
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        # If snake length exceeds its current length, remove the tail
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Draw the snake and food
        print_snake(snake_block, snake_list)
        display.blit(image, (food_x, food_y))  # Draw food (coin)

        # Display score and level
        display_score_and_level(score, level)

        # Update the screen
        pygame.display.update()

        # Control the game speed (higher speed with each level)
        clock.tick(speed)

    pygame.quit()

# Function to draw the snake
def print_snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(display, black, [segment[0], segment[1], snake_block, snake_block])

# Run the main function to start the game
main()
