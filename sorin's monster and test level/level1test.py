try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import sys, time, random, math
from pygame import *

from Player2 import *
from Timer import *
from drawPlatforms import *
from Monster import *
from LevelBackground import *
from Menu import *
#from Level import *
from Interaction import *
from Vector import *
from drawPlatforms import *
from Timer import *
from LifeBar import *
from Flood import *
from GameOver import  *
from ScoreCounter import *

mixer.init()


lv1background = LevelBackground('https://i.imgur.com/Q7tBgIc.png')

framecount = 0
interactions = []
addedInteractions = False
numberOfPlatforms = 0
numberOfGoats=0
platforms = drawPlatforms("hard", 9)
numberOfPlatforms += platforms.platform
drawPlayer = len(platforms.coords)
if drawPlayer % 2 != 0:
    drawPlayer += 1
drawPlayer //=2
drawPlayer = Vector(platforms.coords[drawPlayer-1].p1.x,700-platforms.coords[drawPlayer-1].p1.y)
player1 = Player2(drawPlayer, "https://i.imgur.com/2cnk4Yx.png", 496, 1160, 10, 4, 'w', 'a', 's', 'd', 'up',
                  'left', 'right', 0, 3)
goats = []
numberOfPlatforms += platforms.platform - 1
scoreCount = ScoreCounter(player1)
lifeBar = LifeBar(player1)
print(numberOfPlatforms)
flood = Flood(player1)
removedLife = True
def draw(canvas):
    global interactions, addedInteractions, numberOfPlatforms, framecount, timer,numberOfGoats,goats,removedLife,scoreCount
    if framecount % 120 == 0 and framecount !=0:
        removedLife = False
    time = Timer()
    lv1background.update(canvas)
    platforms.draw(canvas)
    time.draw(canvas)
    scoreCount.update(canvas)
    lifeBar.update(canvas)
    flood.draw(canvas)

    if not addedInteractions:
        for i in range(len(platforms.getCoords())):
            interaction = Interaction(player1, platforms.coords[i])
            interactions.append(interaction)
        addedInteractions = True

    for i in range(len(platforms.getCoords())):
        platforms.coords[i].p1 = Vector(platforms.coords[i].getp1().getP()[0],
                                        platforms.coords[i].getp1().getP()[1] + 1)
        platforms.coords[i].p2 = Vector(platforms.coords[i].getp2().getP()[0],
                                        platforms.coords[i].getp2().getP()[1] + 1)

        tempPlatform = Platform2(0)
        if platforms.coords[i].p1.y > 700:
            platforms.coords.pop(i)
            if i > 1:
                while not (abs(tempPlatform.getx1() - platforms.coords[
                        i - 1].getx1()) > platforms.DISTANCE * platforms.difficulty or \
                                       abs(tempPlatform.getx2() - platforms.coords[
                                               i - 1].getx2()) > platforms.DISTANCE * platforms.difficulty):
                    tempPlatform = Platform2(0)
            platforms.coords.insert(i, tempPlatform)
            tempInteraction = Interaction(player1, tempPlatform)
        else:
            tempInteraction = Interaction(player1, platforms.coords[i])
        interactions.pop(i)
        interactions.insert(i, tempInteraction)
        if random.randint(0,1) > 0.5 and framecount % 60 == 0 and numberOfGoats <3 and platforms.coords[i].p1.y < player1.pos.y :  # numberOfPlatforms % 5 == 0 and not madeGoat
            makeGoat(platforms.coords[i])
            numberOfGoats+=1
        goatsToPop = []
        for j in range(len(goats)):
            if platforms.coords[i] == goats[j].platform:
                goats[j].pos = Vector(goats[j].pos.x,platforms.coords[i].p1.y-platforms.coords[i].thickness-goats[j].frameHeight/2)
                goats[j].update(canvas)
            if goats[j].isColliding(player1):
                print(goats[j].hit(player1))
                if goats[j].hit(player1):
                    goatsToPop.append(goats[j])
                    numberOfGoats -= 1
                    player1.scoreCount+=100
                elif not removedLife:
                    player1.lifePoints-=1
                    print("lives:",player1.lifePoints)
                    removedLife = True
            if goats[j].pos.y > 630:
                goatsToPop.append(goats[j])
                numberOfGoats-=1
        for j in range(len(goatsToPop)):
            goats.remove(goatsToPop[j])

    framecount += 1

    for i in range(len(interactions)):

        if platforms.coords[i].covers(player1.pos):
            interactions[i].update()
    platforms.draw(canvas)
    player1.update(canvas)


def makeGoat(platform):
    global goats
    goat = Monster(2, player1, platform)
    goats.append(goat)


def keyUp(key):
    player1.keyUp(key)


def keyDown(key):
    player1.keyDown(key)


def KeyDown(key):
    player1.keyDown(key)




frame = simplegui.create_frame("Menu", 500, 700)
menu = Menu(frame)
frame.set_mouseclick_handler(menu.play_button.mouse_handler)
frame.set_draw_handler(menu.drawMenu)
frame.start()
if menu.play_button.action:
    level = 1.5
    if level == 1:
        mixer.music.load("All Star 8 Bit.mp3")
        mixer.music.play(-1)
    elif level == 1.5:
        mixer.music.load("harder_better_faster_stronger.mp3")
        mixer.music.play(-1)
    elif level == 2:
        mixer.music.load("Feel Good Inc. [8 Bit Tribute to Gorillaz] - 8 Bit Universe.mp3")
        mixer.music.play(-1)

    frame.stop()
    frame = simplegui.create_frame("Half-Life 3", 500, 700)
    frame.set_draw_handler(draw)
    frame.set_keyup_handler(keyUp)
    frame.set_keydown_handler(keyDown)
    frame.start()
if player1.pos.y > 660:
    pass
    #player1.lifePoints = 0

if player1.lifePoints <= 0:
    gameOver = GameOver((250, 350))
    frame.stop()
    # mixer.music.load("Dark Souls - You Died Sound Effect.mp3")
    # mixer.music.play(0)
    frame = simplegui.create_frame("Half-Life 3", 500, 700)
    frame.set_draw_handler(gameOver.draw)
    frame.start()
