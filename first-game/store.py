import pygame
import pygame.freetype
import sys
import random
import lvlGen as LG
import thanks
import notEnough as NE
pygame.init()

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
maroon = (94, 8, 8)
teal = (0, 255, 242)
rgb = random.choice([red, green, blue])

takeaway1 = 20
takeaway2 = 30
takeaway3 = 40
takeaway4 = 50

def storeLoad():
    global red, green, blue, rgb, takeaway1, takeaway2
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    background = pygame.image.load('menuBackground.png')
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("test")
    black = (0, 0, 0)
    font = pygame.font.SysFont('Minecraft', 30)
    text3 = font.render('You have: ' + str(LG.numcollected) + " coins!", False, red)
    text4 = font.render('Blue Skin - 20 Coins', False, red)
    text5 = font.render('Hit LEFT ARROW to go back to the game!', False, red)
    text6 = font.render('R G B SQUARE!!!! - 30 Coins', False, red)
    text7 = font.render('Maroon Skin - 40 Coins', False, red)
    text8 = font.render('Teal Skin - 50 Coins', False, red)
    center = (0, 0)
    while True:
        screen.blit(background, center)
        screen.blit(text3, (5, 15))
        screen.blit(text5, (5, 580))
        screen.blit(text4, (20, 110))
        screen.blit(text6, (20, 210))
        screen.blit(text7, (20, 310))
        screen.blit(text8, (20, 410))
        pygame.draw.rect(screen, blue, (20, 50, 60, 60))
        pygame.draw.rect(screen, rgb, (20, 150, 60, 60))
        pygame.draw.rect(screen, maroon, (20, 250, 60, 60))
        pygame.draw.rect(screen, teal, (20, 350, 60, 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            LG.levelGen()
        if pressed[pygame.K_1]:
            buyItem1()
        if pressed[pygame.K_2]:
            buyItem2()
        if pressed[pygame.K_3]:
            buyItem3()
        if pressed[pygame.K_4]:
            buyItem4()

        pygame.display.update()

def buyItem1():
    global takeaway1
    if LG.numcollected >= 20:
        LG.numcollected -= takeaway1
        LG.playerColor = LG.blue
        thanks.thanksForPurchase()
    else:
        NE.notEnoughCoins()

def buyItem2():
    global takeaway2
    if LG.numcollected >= 30:
        LG.numcollected -= takeaway2
        LG.playerColor = LG.rgb
        thanks.thanksForPurchase()
    else:
        NE.notEnoughCoins()

def buyItem3():
    global takeaway3
    if LG.numcollected >= 40:
        LG.numcollected -= takeaway3
        LG.playerColor = LG.maroon
        thanks.thanksForPurchase()
    else:
        NE.notEnoughCoins()

def buyItem4():
    global takeaway4
    if LG.numcollected >= 50:
        LG.numcollected -= takeaway4
        LG.playerColor = LG.teal
        thanks.thanksForPurchase()
    else:
        NE.notEnoughCoins()

