
try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import sys, time, random, math
from Vector import *
from Platform import *
import Player2
from Player2 import *
from Interaction import *
from drawPlatforms import *
from Player import *
from LevelBackground import *
from Menu import *
from Level import *


from pygame import *

mixer.init()

from pygame import *

player1 = Player2(Vector(400, 400), "https://i.imgur.com/2cnk4Yx.png", 496, 1160, 10, 4, 'w', 'a', 's', 'd', 'up',
                  'left', 'right', 10, 3)
platforms = drawPlatforms("hard", 7)
lv1 = LevelBackground('https://i.imgur.com/Q7tBgIc.png')

interactions = []
addedInteractions = False


def draw(canvas):
    global interactions, addedInteractions
    lv1.update(canvas)
    platforms.draw(canvas)

    if not addedInteractions:
        for i in range(len(platforms.getCoords())):
            interaction = Interaction(player1, platforms.coords[i])
            interactions.append(interaction)
        addedInteractions = True

    for i in range(len(platforms.getCoords())):
        platforms.coords[i].p1 = Vector(platforms.coords[i].getp1().getP()[0],
                                        platforms.coords[i].getp1().getP()[1] + 0.5)
        platforms.coords[i].p2 = Vector(platforms.coords[i].getp2().getP()[0],
                                        platforms.coords[i].getp2().getP()[1] + 0.5)

        tempPlatform = Platform2(0)
        if platforms.coords[i].p1.getP()[1] > 700:
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

    for i in range(len(interactions)):

        if platforms.coords[i].covers(player1.pos):
            interactions[i].update()
            # print("i: ",i)

    platforms.draw(canvas)
    player1.update(canvas)


def keyUp(key):
    player1.keyUp(key)


def keyDown(key):
    player1.keyDown(key)





##play method that 
play_endless = False
while play_endless == False:
    try:
      menu = Menu()
      break
    except TypeError:


        level = Level(1)
        if level.getLevel() == 1:
            mixer.music.load("All Star 8 Bit.mp3")
            mixer.music.play(-1)
        elif level.getLevel() == 1.5:
            mixer.music.load("harder_better_faster_stronger.mp3")
            mixer.music.play(-1)
        elif level.getLevel() == 2:
            mixer.music.load("Thriller (8 Bit).mp3")
            mixer.music.play(-1)


        frame = simplegui.create_frame('Half-Life 3', 500, 700)
        frame.set_draw_handler(draw)
        frame.set_keyup_handler(keyUp)
        frame.set_keydown_handler(keyDown)
        frame.start()

        play_endless = True



