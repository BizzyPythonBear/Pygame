import pygame
import pygame.freetype
import sys
import random
from time import sleep
import lvlGen as LG
import store as ST

pygame.init()


def nextLevel():
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    background = pygame.image.load(
        'menuBackground.png')
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("test")
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font = pygame.font.SysFont('Minecraft', 30)
    text2 = font.render('Hit SPACE to proceed', False, red)
    text5 = font.render('Hit ENTER to go to the store!', False, red)
    text3 = font.render("You've completed level: " + str(LG.levelsCompleted) + "! Continue?", False, red)
    text4 = font.render("You now have: " + str(LG.numcollected) + " coins!", False, red)
    center = (0, 0)
    while True:
        screen.blit(background, center)
        screen.blit(text3, (400, 300))
        screen.blit(text2, (400, 200))
        screen.blit(text4, (400, 400))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            LG.levelGen()
        if pressed[pygame.K_INSERT]:
            ST.storeLoad()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
