try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from PlatformItem import PlatformItem

class FireTrap(PlatformItem):

    def __init__(self, pos, player):

        self.frameIndex = (0, 15)
        self.topFrameRow = 15
        self.lastFrameRow = 15
        self.spritePlaySpeed = 5

        PlatformItem.__init__(self, pos, player)

# update , imgupdate and collide method can be used as exists in PlatformItem superclass

def draw(canvas):
    fire.update(canvas)

fire = FireTrap((500, 500), 'adfsda')
frame = simplegui.create_frame("safdasdfsdaf", 1000, 1000)
frame.set_draw_handler(draw)
frame.start()


