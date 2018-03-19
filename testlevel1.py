try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import sys, time, random, math
from pygame import *

from Player2 import  *
from Interaction import *
from drawPlatforms import  *
from Monster import *
from LevelBackground import LevelBackground
from Menu import Menu
from Level import Level
from Interaction import Interaction
from Vector import Vector
from drawPlatforms import drawPlatforms
mixer.init()


player1 = Player2(Vector(400,400),"https://i.imgur.com/2cnk4Yx.png",496,1160,10,4,'w','a','s','d','up','left','right',10,3)
lv1background = LevelBackground('https://i.imgur.com/Q7tBgIc.png')
#platform2 = Platform2(500)



# for i in range(len(platforms.coords)-1):
#     interaction = Interaction(player1,platforms.coords[i])
#     interactions.append(interaction)

#player2 = Player(Vector(50,50),"https://i.imgur.com/fDEbrVB.png",256,256,2,2,'up','left','down','right','space',10)
#platform1 = Platform("hard")
interactions = []
addedInteractions = False
numberOfPlatforms = 0
madeGoat = False
monsters = []
platforms = drawPlatforms("hard",9)
numberOfPlatforms+=platforms.platform-1
framecount = 0
print(numberOfPlatforms)
# for i in range(len(platforms.getCoords()) - 1):
#     interaction = Interaction(player1, platforms.coords[i])
#     interactions.append(interaction)
#print("len interactions: ", len(interactions))
def draw(canvas):
    global interactions , addedInteractions, numberOfPlatforms , madeGoat,framecount
    lv1background.update(canvas)
    platforms.draw(canvas)
    if not addedInteractions:
        for i in range(len(platforms.getCoords()) ):
            interaction = Interaction(player1, platforms.coords[i])
            interactions.append(interaction)
        addedInteractions = True
    #platform2.draw(canvas)
    for i in range(len(platforms.getCoords())):
        platforms.coords[i].p1 = Vector(platforms.coords[i].getp1().getP()[0],platforms.coords[i].getp1().getP()[1] + 1)
        platforms.coords[i].p2 = Vector(platforms.coords[i].getp2().getP()[0],platforms.coords[i].getp2().getP()[1] + 1)
        #print("platform: ",platforms.coords[i])
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
            #print(platforms.coords[i])
            #print(monsters[j].platform)
            if platforms.coords[i] == monsters[j].platform:
                monsters[j].pos = Vector(monsters[j].pos.x,platforms.coords[i].p1.y-platforms.coords[i].thickness-monsters[j].frameHeight/2)
                #print("goat position: ",monsters[j].pos.y)
                monsters[j].update(canvas)
            if monsters[j].pos.y > 630:
                #print("popped")
                monsters.pop(j)
                #print(len(monsters))
                madeGoat = False
    framecount+=1
        #print("inserted new interaction:",platforms.coords[i])

    for i in range(len(interactions)):
        # print(len(interactions))
        # print("coords: ",len(platforms.coords))
        #print(platforms.coords[i].covers(player1.pos))
        #print(player1.pos.getP()[1]-player1.frameHeight/2<platforms.coords[i].p1.getP()[1])   and pos.getP()[1]<self.yCoord    //and player1.pos.getP()[1]-player1.frameHeight<platforms.coords[i].p1.getP()[1]
        #distPlayerPlat = platforms.coords[i].p1.getP()[1] - player1.pos.getP()[1]-player1.frameHeight
        if platforms.coords[i].covers(player1.pos) :#and player1.pos.getP()[1]-player1.frameHeight<platforms.coords[i].p1.getP()[1]:
            interactions[i].update()
            #print("i: ",i)


    #canvas.draw_line(player1.getCoordinates().getP(),platform2.p1.getP(),3,"blue")
    #canvas.draw_line(player1.getCoordinates().getP(),platform2.p2.getP(),3,"blue")
    platforms.draw(canvas)
    #canvas.draw_line((player1.getCoordinates() + Vector(0,player1.frameHeight/2)).getP(),(abs(platform2.p2.x - platform2.p1.x),platform2.p1.y),3,"yellow")
    #platform1.draw(canvas)
    #player2.update(canvas)
    player1.update(canvas)
def makeGoat(platform):
    global monsters
    goat = Monster( 2, player1, platform)
    monsters.append(goat)
def keyUp(key):
    player1.keyUp(key)
    #player2.keyUp(key)
def keyDown(key):
    player1.keyDown(key)
    #player2.keyDown(key)

def KeyDown(key):
    player1.eyDown(key)

play_endless = False
while play_endless == False:
    try:
        menu = Menu()
        break
    except TypeError:

        level = Level(1)
        if level.getLevel() == 1:
            mixer.music.load("All Star.mp3")
            mixer.music.play(-1)
        elif level.getLevel() == 1.5:
            mixer.music.load("Harder Better Faster Stronger.mp3")
            mixer.music.play(-1)
        elif level.getLevel() == 2:
            mixer.music.load("Feel Good Inc.mp3")
            mixer.music.play(-1)

frame = simplegui.create_frame("Half-Life 3",500,700)
frame.set_draw_handler(draw)
frame.set_keyup_handler(keyUp)
frame.set_keydown_handler(keyDown)
frame.start()