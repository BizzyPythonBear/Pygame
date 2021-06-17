import pygame
import pygame.freetype
import sys
import random
from time import sleep
import lvlGen as LG
pygame.init()

red = (255, 0, 0)

def notEnoughCoins():
    global red
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    background = pygame.image.load('menuBackground.png')
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("test")
    font = pygame.font.SysFont('Minecraft', 30)
    text3 = font.render("You don't have enough coins! Sending you back to main game...", False, red)
    while True:
        screen.blit(background, (0,0))
        screen.blit(text3, (5, 15))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        pygame.display.update()

        def goto():
            LG.levelGen()

        sleep(1)
        goto()