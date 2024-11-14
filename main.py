from math import sin, cos, pi
import pygame

screen_width = 1024
screen_height = 512

player_x = 300
player_y = 300
player_size = 8
player_angle = 0
player_dx = 0
player_dy = 0

world_width = 8
world_height = 8
block_size = 64

world = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    start = 0
    stop = 0
    for i in range(world_width):
        for j in range(world_height):
            color = "black"
            if world[i][j] == 1:
                color = "white"
            start = i * block_size
            stop = j * block_size
            pygame.draw.rect(screen, color, pygame.Rect(start + 1, stop + 1, block_size - 1, block_size - 1))
    player_color = "green"
    pygame.draw.rect(screen, player_color, pygame.Rect(player_x - player_size/2, player_y - player_size/2, player_size, player_size))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_x += player_dx
        player_y += player_dy
    if keys[pygame.K_s]:
        player_x -= player_dx
        player_y -= player_dy
    if keys[pygame.K_a]:
        player_angle -= 0.1
        if player_angle < 0:
            player_angle += 2 * pi
        player_dx = cos(player_angle) * 2
        player_dy = sin(player_angle) * 2
    if keys[pygame.K_d]:
        player_angle += 0.1
        if player_angle > 2*pi:
            player_angle += 2 * pi
        player_dx = cos(player_angle) * 2
        player_dy = sin(player_angle) * 2
    pygame.draw.line(screen, "orange", (player_x, player_y), (player_x + player_dx*8, player_y + player_dy*8), width=2)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()