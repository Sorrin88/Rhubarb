try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from PlatformItem import PlatformItem


class SpeedUpItem(PlatformItem):

    def __init__(self, pos, player):

        self.frameIndex = (0, 7)
        self.topFrameRow = 7
        self.lastFrameRow = 10
        self.spritePlaySpeed = 3

        PlatformItem.__init__(self, pos, player)

#update , imgupdate and collide method can be used as exists in PlatformItem superclass

def draw(canvas):
    speed.update(canvas)


speed = SpeedUpItem((500, 500), 'adfsda')
frame = simplegui.create_frame("safdasdfsdaf", 1000, 1000)
frame.set_draw_handler(draw)
frame.start()
