import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake initial position and direction
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction

# Food spawn position
food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
food_spawn = True

# Score
score = 0

# Clock for game speed
clock = pygame.time.Clock()

# Game Over Function
def game_over():
    my_font = pygame.font.SysFont("times new roman", 48)
    game_over_surface = my_font.render("Game Over", True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width / 2, screen_height / 4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.quit()
    quit()

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not (snake_direction == "DOWN"):
                    change_to = "UP"
            elif event.key == pygame.K_DOWN:
                if not (snake_direction == "UP"):
                    change_to = "DOWN"
            elif event.key == pygame.K_LEFT:
                if not (snake_direction == "RIGHT"):
                    change_to = "LEFT"
            elif event.key == pygame.K_RIGHT:
                if not (snake_direction == "LEFT"):
                    change_to = "RIGHT"

    # Update snake direction
    snake_direction = change_to

    # Move the snake
    if snake_direction == "UP":
        snake_pos[1] -= 10
    elif snake_direction == "DOWN":
        snake_pos[1] += 10
    elif snake_direction == "LEFT":
        snake_pos[0] -= 10
    elif snake_direction == "RIGHT":
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (screen_width//10)) * 10, random.randrange(1, (screen_height//10)) * 10]
    food_spawn = True

    # Game Over conditions
    if snake_pos[0] < 0 or snake_pos[0] >= screen_width or snake_pos[1] < 0 or snake_pos[1] >= screen_height:
        game_over()
    for segment in snake_body[1:]:
        if snake_pos[0] == segment[0] and snake_pos[1] == segment[1]:
            game_over()

    # Draw Snake and Food
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Draw Score
    my_font = pygame.font.SysFont("times new roman", 24)
    score_surface = my_font.render("Score: " + str(score), True, white)
    score_rect = score_surface.get_rect()
    score_rect.topleft = (screen_width - 120, 10)
    screen.blit(score_surface, score_rect)

    pygame.display.flip()

    # Game Speed
    clock.tick(10)