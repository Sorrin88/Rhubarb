try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
import  sys, time, random,math
from Vector import *
from Player import *
player1 = Player(Vector(10,10),"https://i.imgur.com/fDEbrVB.png",'w','a','s','d',10)

frame = simplegui.create_frame("Half-Life 3",500,500)
frame.set_draw_handler(player1.update)
frame.set_keyup_handler(player1.keyUp)
frame.set_keydown_handler(player1.keyDown)
frame.start()