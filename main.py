import pygame
from config import *
from tetromino import Tetromino
from game import Game

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
game = Game()
fall_time = 0
fall_speed = 100  # accurate with NES Tetris LVL9

running = True
while running:
    dt = clock.tick(60)
    fall_time += dt
    if fall_time > fall_speed:
        game.update()
        fall_time = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                game.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                game.move(1, 0)
            elif event.key == pygame.K_DOWN:
                game.move(0, 1)
            elif event.key == pygame.K_z:
                game.rotate('left')
            elif event.key == pygame.K_x or event.key == pygame.K_UP:
                game.rotate('right')

    game.draw(screen)
    pygame.display.flip()

    if game.game_over:
        print("Game Over")
        pygame.time.wait(2000)
        running = False

pygame.quit()
