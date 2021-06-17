import pygame
import pygame.freetype
import sys
import random
from time import sleep
import nextLvl as IDIOT
from died import *
import store
import thanks
pygame.init()
levelsCompleted = 0
totalCoins = 0
numcollected = 0
ran = False
green = (0,255,0)
blue = (0,0,255)
maroon = (94, 8, 8)
teal = (0, 255, 242)
rgb = store.rgb
playerColor = green

def levelGen():
    global levelsCompleted
    global totalCoins
    global ran
    global numcollected
    global playerColor
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
            pygame.draw.rect(screen, playerColor, (self.x, self.y, 20, 20))

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
            self.levelsCompleted = 0
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
        global totalCoins
        totalCoins += numcollected
        ran = False
        return

    def killPlayer():
        player.x = 900
        player.y = 900

    def refresh():
        global totalCoins
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
        levels.updateCount(levelsCompleted)
        pygame.display.update()

    def collectSFX():
        pygame.mixer.Sound.play(coinSFX)
        pygame.mixer.music.stop()

    def triggerSFX():
        pygame.mixer.Sound.play(oneUP)
        return
          
    while running:
        global numcollected
        refresh()
        if player.numcollected == 5:
            if oneUPPlayed:
                oneUPPlayed = False
                triggerSFX()
        if player.numcollected == 10:
            levelsCompleted += 1
            totalCoins += 10
            IDIOT.nextLevel()
            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
                break

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
                numcollected += 1
                coin.collected = True
                collectSFX()
                coin.moveCoinToNewPos()  # Calling new function

        if coin.collected == True:
            coin.draw()

        if pwrUp.collected:
            player.velocity += 0
