import pygame
import pygame.freetype
import sys
import random
from time import sleep
import lvlGen as LG

pygame.init()


def nextLevel():
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    background = pygame.image.load(
        'c:\\Users\\bizze\\Documents\\Python\\Misc\\Pygame\\first-game\\images\\menuBackground.png')
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("test")
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font = pygame.font.SysFont('Minecraft', 30)
    text = font.render('Game Over!', False, red)
    text2 = font.render('Hit SPACE to proceed', False, red)
    text3 = font.render("You've completed a level! Continue?", False, red)
    center = (0, 0)
    while True:
        screen.blit(background, center)
        screen.blit(text3, (400, 300))
        screen.blit(text2, (400, 200))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            LG.levelGen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
