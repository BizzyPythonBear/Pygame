import pygame
import pygame.freetype
import sys
import random
from os import path
import json
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

ran = False

data = {
    'levelsCompleted': 0, #0
    'playerColor': green, #1
    'numcollected': 0, #2
    'totalCoins': 0 #3
}

with open('save_data.txt') as save_data:
    data = json.load(save_data)
    
levelsCompleted = data['levelsCompleted']
playerColor = data['playerColor']
numcollected = data['numcollected']
totalCoins = data['totalCoins']

def levelGen():
    global green
    global ran
    global totalCoins
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    randbackground = random.choice(
        ['background.png', 'level2bckgrn.png', 'level3bckgrnd.png'])
    background = pygame.image.load(randbackground)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("test")
    coinSFX = pygame.mixer.Sound("coinPick.wav")
    oneUP = pygame.mixer.Sound("1UP.wav")
    spikeNum = random.randint(0, 20)
    coinNum = random.randint(0, 10)
    powerUpNum = random.randint(0, 2)
    oneUPPlayed = True
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    black = (0, 0, 0)
    font = pygame.font.SysFont('Minecraft', 30)
    text = font.render('Game Over!', False, red)
    text2 = font.render('Hit SPACE to restart', False, red)
    center = (0, 0)
    running = True
    restart = False

    class Coin:
        def __init__(self):
            self.x = random.randint(0, 500)
            self.y = random.randint(0, 500)
            self.collected = False

        def draw(self):
            pygame.draw.circle(screen, (255, 255, 0), (self.x, self.y), 5)

        # Added this new function that is called when a coin is collected, and changes its x and y position to another random place on the screen
        def moveCoinToNewPos(self):
            self.x = random.randint(0, 500)
            self.y = random.randint(0, 500)
            self.collected = False

    class Player:
        def __init__(self):
            self.x = 250
            self.y = 250
            self.velocity = 1.3
            self.numcollected = 0

        def draw(self):
            pygame.draw.rect(screen, data['playerColor'], (self.x, self.y, 20, 20))

    class ScoreBar:
        def __init__(self, x, width):
            self.x = x
            self.width = width
            self.text = ""

        def updatescore(self, score):
            font = pygame.font.SysFont('Arial', 20)
            self.text = str(score)
            pygame.draw.rect(screen, (0, 255, 0), (self.x, 5, self.width, 12))
            text = font.render(self.text, 1, (255, 255, 255))
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                        5 + (12 / 2 - text.get_height() / 2)))

    class Spike:
        def __init__(self):
            self.x = random.randint(0, 500)
            self.y = random.randint(0, 500)

        def draw(self):
            pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 20, 20))

    class powerUp:
        def __init__(self):
            self.x = random.randint(0, 500)
            self.y = random.randint(0, 500)
            self.collected = False

        def draw(self):
            pygame.draw.circle(screen, blue, (self.x, self.y), 5)

    class levelCounter:
        def __init__(self, x, width):
            self.x = x
            self.width = width
            self.text = ""
        def updateCount(self, score):
            font = pygame.font.SysFont('Arial', 20)
            self.text = str(score)
            pygame.draw.rect(screen, green, (self.x, 5, self.width, 12))
            text = font.render(self.text, 1, (255,255,255))
            screen.blit(text, (self.x + (self.width / 2 - text.get_width() / 2),
                               5 + (12 / 2 - text.get_height() / 2)))

    player = Player()
    coins = []
    spikes = []
    powerUps = []
    pwrUp = powerUp()
    score = ScoreBar(5, 15)
    levels = levelCounter(20, 15)
    coin = Coin()

    for i in range(coinNum):
        c = Coin()
        coins.append(c)
    for i in range(spikeNum):
        s = Spike()
        spikes.append(s)
    for i in range(powerUpNum):
        p = powerUp()
        powerUps.append(p)

    def addCoinsWhenDead():
        data['totalCoins'] += data['numcollected']
        ran = False
        return

    def killPlayer():
        player.x = 900
        player.y = 900

    youDied

    def refresh():
        global ran
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        player.draw()
        for coin in coins:
            if not coin.collected:
                coin.draw()
        for spike in spikes:
            spike.draw()
        for powerUp in powerUps:
            powerUp.draw()

        for spike in spikes:
            if spike.x >= player.x and spike.x <= (player.x+20) and spike.y >= player.y and spike.y <= player.y + 20:
                player.velocity = 0
                restart = True
                ran = True
                kill = True
                while ran:
                    addCoinsWhenDead()
                    ran = False
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                            sys.exit()
                            break
                killPlayer()
                youDied()

        for powerUp in powerUps:
            if powerUp.x >= player.x and powerUp.x <= (player.x+20) and powerUp.y >= player.y and powerUp.y <= player.y + 20:
                player.velocity += 0.5
                powerUp.collected = True

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            restart = True
            levelGen()
            if restart:
                levelGen()
            if not restart:
                return

        score.updatescore(player.numcollected)
        levels.updateCount(data['levelsCompleted'])
        pygame.display.update()

    def collectSFX():
        pygame.mixer.Sound.play(coinSFX)
        pygame.mixer.music.stop()

    def triggerSFX():
        pygame.mixer.Sound.play(oneUP)
        return
          
    while running:
        global levelsCompleted
        global numcollected
        refresh()
        if player.numcollected == 5:
            if oneUPPlayed:
                oneUPPlayed = False
                triggerSFX()
        if player.numcollected == 10:
            data['levelsCompleted'] += 1
            data['totalCoins'] += 10
            nextLevel()
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                with open('save_data.txt','w') as save_data:
                    json.dump(data,save_data)

                running = False
                pygame.quit()
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            player.y -= player.velocity
        if pressed[pygame.K_DOWN]:
            player.y += player.velocity
        if pressed[pygame.K_LEFT]:
            player.x -= player.velocity
        if pressed[pygame.K_RIGHT]:
            player.x += player.velocity

        for coin in coins:
            if coin.x >= player.x and coin.x <= (player.x+20) and coin.y >= player.y and coin.y <= player.y + 20:
                player.numcollected += 1
                data['numcollected'] += 1
                coin.collected = True
                collectSFX()
                coin.moveCoinToNewPos()  # Calling new function

        if coin.collected == True:
            coin.draw()

        if pwrUp.collected:
            player.velocity += 0

def nextLevel():
    global levelsCompleted
    global numcollected
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    levelsCompleted = data['levelsCompleted']
    numcollected = data['numcollected']
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
    text5 = font.render('Hit INSERT to go to the store!', False, red)
    text3 = font.render("You've completed level: " + str(levelsCompleted) + "! Continue?", False, red)
    text4 = font.render("You now have: " + str(numcollected) + " coins!", False, red)
    center = (0, 0)
    while True:
        print(levelsCompleted)
        print(numcollected)
        screen.blit(background, center)
        screen.blit(text3, (400, 300))
        screen.blit(text2, (400, 200))
        screen.blit(text4, (400, 400))
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            levelGen()
        if pressed[pygame.K_INSERT]:
            storeLoad()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break

def storeLoad():
    global red, green, blue, rgb, takeaway1, takeaway2, takeaway3, takeaway4, totalCoins, numcollected, levelsCompleted, playerColor
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    background = pygame.image.load('menuBackground.png')
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("test")
    black = (0, 0, 0)
    font = pygame.font.SysFont('Minecraft', 30)
    text3 = font.render('You have: ' + str(numcollected) + " coins!", False, red)
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
            levelGen()
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
    global numcollected
    if numcollected >= 20:
        data['numcollected'] -= takeaway1
        data['playerColor'] = blue
        thanks.thanksForPurchase()
    else:
        NE.notEnoughCoins()

def buyItem2():
    global takeaway2
    global numcollected
    if numcollected >= 30:
        data['numcollected'] -= takeaway2
        data['playerColor'] = rgb
        thanks.thanksForPurchase()
    else:
        NE.notEnoughCoins()

def buyItem3():
    global takeaway3
    global numcollected
    if numcollected >= 40:
        data['numcollected'] -= takeaway3
        data['playerColor'] = maroon
        thanks.thanksForPurchase()
    else:
        NE.notEnoughCoins()

def buyItem4():
    global takeaway4
    global numcollected
    if numcollected >= 50:
        data['numcollected'] -= takeaway4
        data['playerColor'] = teal
        thanks.thanksForPurchase()
    else:
        NE.notEnoughCoins()

def youDied():
    global data, numcollected
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
    text3 = font.render('You collected: ' + str(data["numcollected"]) + " coins!", False, red)
    while True:
        screen.fill(black)
        screen.blit(text, (400, 300))
        screen.blit(text2, (400, 200))
        screen.blit(text3, (400, 400))

        pygame.display.update()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE]:
            levelGen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
