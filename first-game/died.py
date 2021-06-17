import pygame
import pygame.freetype
import sys
import random
import lvlGen as LG

def youDied():
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("test")
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font = pygame.font.SysFont('Minecraft', 30)
    text = font.render('Game Over!', False, red)
    text2 = font.render('Hit SPACE to restart', False, red)
    text3 = font.render('You collected: ' + str(LG.numcollected) + " coins!", False, red)
    while True:
        screen.fill(black)
        screen.blit(text, (400, 300))
        screen.blit(text2, (400, 200))
        screen.blit(text3, (400, 400))

        pygame.display.update()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            LG.levelGen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break