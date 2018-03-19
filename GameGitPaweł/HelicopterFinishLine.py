try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from FinishLine import FinishLine

class HelicopterFinishLine(FinishLine):

    def __init__(self, pos, player):

        self.frameIndex = (0, 0)
        self.topFrameRow = 0
        self.lastFrameRow = 2
        self.spritePlaySpeed = 5

        FinishLine.__init__(self, pos, player)

# update , imgupdate and collide method can be used as exists in PortalFInishLine superclass

def draw(canvas):
    helicopter.update(canvas)

helicopter = HelicopterFinishLine((500, 100), 'adfsda')
frame = simplegui.create_frame("safdasdfsdaf", 599, 700)
frame.set_draw_handler(draw)
frame.start()


