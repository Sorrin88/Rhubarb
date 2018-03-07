try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector
from LineMove import LineMove

myLine = LineMove((Vector(0,0)), (Vector(600,0)))
myLine2 = LineMove((Vector(0,0)), (Vector(700,0)))

frame = simplegui.create_frame("Half-Life 3",500,500)
frame.set_draw_handler(myLine.update)
frame.start()