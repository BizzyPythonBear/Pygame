import pygame
import pygame.freetype
import sys
import random
from time import sleep
from lvlGen import *
pygame.init()


def mainMenu():
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    background = pygame.image.load(
        'c:\\Users\\bizze\\Documents\\Python\\Misc\\Pygame\\first-game\\images\\menuBackground.png')
    font = pygame.font.SysFont('Minecraft', 30)
    text = font.render('Coin Collect Game!', False, red)
    text2 = font.render('Hit SPACE to start!', False, red)
    while True:
        screen.blit(background, (0, 0))
        screen.blit(text, (400, 300))
        screen.blit(text2, (400, 200))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            levelGen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break


mainMenu()  # Runs main menu on startup so it shows up before the actual game

# Hello there, this is just here so I can get passed the 700th line
# And yes, I know there is a lot of duplicated code, but in my defense,
# I only duplicated the code to make it easier for me to add extra levels.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#-= COMING UP =-#
# - Better Main Menu
# - Upgrades
#-=-=-=-=-=-=-=-#
