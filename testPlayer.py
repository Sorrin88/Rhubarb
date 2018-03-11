try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector
from Player import Player
from ChickenMonster import ChickenMonster
from Monster import Monster

IMAGEWIDTH = 500
IMAGEHEIGHT = 1000

position1 = -500
position2 = 500
timer = 0

player1 = Player(Vector(100,100),"https://i.imgur.com/S1PGJIb.png",256,256,2,2,'w','a','s','d','space',10)
chicken = ChickenMonster(Vector(0,0), 400, 400, 'hard', 2, player1)
goat = Monster(Vector (0,0), 0, 430,'hard', 1)

def draw(canvas):
    player1.update(canvas)
    chicken.update(canvas)
    goat.update(canvas)
    #splayer2.update(canvas)
def keyUp(key):
    player1.keyUp(key)
    #player2.keyUp(key)
def keyDown(key):
    player1.keyDown(key)
    #player2.keyDown(key)

image = simplegui.load_image('https://i.imgur.com/VLZsdso.png')

frame = simplegui.create_frame("Half-Life 3",500,500)
frame.set_draw_handler(draw)
frame.set_keyup_handler(keyUp)
frame.set_keydown_handler(keyDown)
frame.start()