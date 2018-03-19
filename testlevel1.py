try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import sys, time, random, math
from pygame import *

from Player2 import *

from drawPlatforms import *
from Monster import *
from LevelBackground import *
from Menu import *
from Level import *
from Interaction import *
from Vector import *
from drawPlatforms import *
mixer.init()


player1 = Player2(Vector(400,400),"https://i.imgur.com/2cnk4Yx.png",496,1160,10,4,'w','a','s','d','up','left','right',10,3)
lv1background = LevelBackground('https://i.imgur.com/Q7tBgIc.png')


interactions = []
addedInteractions = False
numberOfPlatforms = 0
madeGoat = False
monsters = []
platforms = drawPlatforms("hard", 9)
numberOfPlatforms+=platforms.platform-1
framecount = 0
print(numberOfPlatforms)

def draw(canvas):
    global interactions , addedInteractions, numberOfPlatforms , madeGoat,framecount
    lv1background.update(canvas)
    platforms.draw(canvas)
    if not addedInteractions:
        for i in range(len(platforms.getCoords()) ):
            interaction = Interaction(player1, platforms.coords[i])
            interactions.append(interaction)
        addedInteractions = True

    for i in range(len(platforms.getCoords())):
        platforms.coords[i].p1 = Vector(platforms.coords[i].getp1().getP()[0],platforms.coords[i].getp1().getP()[1] + 1)
        platforms.coords[i].p2 = Vector(platforms.coords[i].getp2().getP()[0],platforms.coords[i].getp2().getP()[1] + 1)

        tempPlatform = Platform2(0)
        if platforms.coords[i].p1.y > 700:
            platforms.coords.pop(i)
            if i > 1:
                while not (abs(tempPlatform.getx1() -platforms.coords[i-1].getx1()) > platforms.DISTANCE*platforms.difficulty or \
                    abs(tempPlatform.getx2() - platforms.coords[i - 1].getx2()) > platforms.DISTANCE * platforms.difficulty):
                        tempPlatform = Platform2(0)
            platforms.coords.insert(i,tempPlatform)
            tempInteraction = Interaction(player1, tempPlatform)
        else:
            tempInteraction = Interaction(player1, platforms.coords[i])
        interactions.pop(i)
        interactions.insert(i,tempInteraction)
        numberOfPlatforms+=1
        if numberOfPlatforms % 5 == 0 and not madeGoat: #numberOfPlatforms % 5 == 0 and not madeGoat
            makeGoat(platforms.coords[len(platforms.coords)-1])
            madeGoat = True
        for j in range(len(monsters)):
            if platforms.coords[i] == monsters[j].platform:
                monsters[j].pos = Vector(monsters[j].pos.x,platforms.coords[i].p1.y-platforms.coords[i].thickness-monsters[j].frameHeight/2)
                monsters[j].update(canvas)
            if monsters[j].pos.y > 630:

                monsters.pop(j)

                madeGoat = False
    framecount += 1


    for i in range(len(interactions)):

        if platforms.coords[i].covers(player1.pos):
            interactions[i].update()




    platforms.draw(canvas)

    player1.update(canvas)
def makeGoat(platform):
    global monsters
    goat = Monster( 2, player1, platform)
    monsters.append(goat)
def keyUp(key):
    player1.keyUp(key)

def keyDown(key):
    player1.keyDown(key)


def KeyDown(key):
    player1.eyDown(key)

play_endless = False
while play_endless == False:
    try:
        menu = Menu()
        break
    except TypeError:

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

        frame = simplegui.create_frame("Half-Life 3",500,700)
        frame.set_draw_handler(draw)
        frame.set_keyup_handler(keyUp)
        frame.set_keydown_handler(keyDown)
        frame.start()
        
        play_endless = True
