import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 720, 480
GRID = 10
SPEED = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 24)
big_font = pygame.font.SysFont("arial", 40)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


def draw_text(text, x, y, color=WHITE, fnt=font, center=False):
    render = fnt.render(text, True, color)
    if center:
        x = (WIDTH - render.get_width()) // 2
    screen.blit(render, (x, y))


def start_menu():
    while True:
        screen.fill(BLACK)
        draw_text("Snake Game :) ", 260, 150, WHITE, big_font, center=True)
        draw_text("Press SPACE to Start", 250, 200, WHITE, font, center=True)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return


def game_over_menu(score):
    while True:
        screen.fill(BLACK)
        draw_text(f"Game Over! Score: {score}", 200, 150, RED, big_font)
        draw_text("R - Restart", 300, 230)
        draw_text("Q - Quit", 320, 270)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "restart"
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()


def game_loop():
    snake = [[100, 50], [90, 50], [80, 50]]
    direction = "RIGHT"

    fruit = [
        random.randrange(1, WIDTH // GRID) * GRID,
        random.randrange(1, HEIGHT // GRID) * GRID
    ]

    score = 0

    while True:
        screen.fill(BLACK)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    direction = "UP"
                if event.key == pygame.K_DOWN and direction != "UP":
                    direction = "DOWN"
                if event.key == pygame.K_LEFT and direction != "RIGHT":
                    direction = "LEFT"
                if event.key == pygame.K_RIGHT and direction != "LEFT":
                    direction = "RIGHT"

        # move snake
        x, y = snake[0]

        if direction == "UP":
            y -= GRID
        if direction == "DOWN":
            y += GRID
        if direction == "LEFT":
            x -= GRID
        if direction == "RIGHT":
            x += GRID

        new_head = [x, y]
        snake.insert(0, new_head)

        # eat fruit
        if new_head == fruit:
            score += 10
            fruit = [
                random.randrange(1, WIDTH // GRID) * GRID,
                random.randrange(1, HEIGHT // GRID) * GRID
            ]
        else:
            snake.pop()

        # draw snake
        for part in snake:
            pygame.draw.rect(screen, GREEN, (*part, GRID, GRID))

        # draw fruit
        pygame.draw.rect(screen, WHITE, (*fruit, GRID, GRID))

        # collision
        if (
            x < 0 or x >= WIDTH or
            y < 0 or y >= HEIGHT or
            new_head in snake[1:]
        ):
            return score

        draw_text(f"Score: {score}", 10, 10)

        pygame.display.update()
        clock.tick(SPEED)


# MAIN FLOW
while True:
    start_menu()
    result = game_loop()
    action = game_over_menu(result)

    if action == "restart":
        continue