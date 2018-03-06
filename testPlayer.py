try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import  sys, time, random,math
from Vector import *
from Player import *
player1 = Player(Vector(250,250),"https://i.imgur.com/fDEbrVB.png",256,256,2,2,'w','a','s','d',10)
player2 = Player(Vector(50,50),"https://i.imgur.com/fDEbrVB.png",256,256,2,2,'up','left','down','right',10)

def draw(canvas):
    player1.update(canvas)
    player2.update(canvas)
def keyUp(key):
    player1.keyUp(key)
    player2.keyUp(key)
def keyDown(key):
    player1.keyDown(key)
    player2.keyDown(key)
frame = simplegui.create_frame("Half-Life 3",500,500)
frame.set_draw_handler(draw)
frame.set_keyup_handler(keyUp)
frame.set_keydown_handler(keyDown)
frame.start()