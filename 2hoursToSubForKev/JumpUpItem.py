try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from PlatformItem import PlatformItem


class JumpUpItem(PlatformItem):

    def __init__(self, pos, player):

        self.frameIndex = (0,11)
        self.topFrameRow = 11
        self.lastFrameRow = 14
        self.spritePlaySpeed = 3

        PlatformItem.__init__(self, pos, player)

#update , imgupdate and collide method can be used as exists in PlatformItem superclass

def draw(canvas):
    jump.update(canvas)


jump = JumpUpItem((500, 500), 'adfsda')
frame = simplegui.create_frame("safdasdfsdaf", 1000, 1000)
frame.set_draw_handler(draw)
frame.start()

