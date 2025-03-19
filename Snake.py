import pygame

blue = (50, 153, 213)
black = (0, 0, 0)
dis_width = 600
dis_height = 400
snake_block = 10

pygame.init()

display = pygame.display.set_mode((dis_width, dis_height))
clock = pygame.time.Clock()


def main():
    game_over = False
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 10
    while not game_over:
        display.fill(blue)
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
        x1 += x1_change
        y1 += y1_change

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        print_snake(snake_block, snake_list)

        if 0 > snake_head[0] > 600 or 0 > snake_head[1] > 400:
            pygame.quit()


        pygame.display.update()
        clock.tick(15)
    pygame.quit()


def print_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, black, [x[0], x[1], snake_block, snake_block])


main()