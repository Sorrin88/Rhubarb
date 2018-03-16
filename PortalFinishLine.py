try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from FinishLine import FinishLine

class PortalFinishLine(FinishLine):

    def __init__(self, pos, player):

        self.frameIndex = (0, 3)
        self.topFrameRow = 0
        self.lastFrameRow = 0
        self.spritePlaySpeed = 5

        FinishLine.__init__(self, pos, player)

#Override update...
    def update(self, canvas):
        if self.collided == False:
            canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                                 self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                              (self.frameWidth, self.frameHeight), self.pos,
                              (self.frameWidth / 8, self.frameHeight / 8))  # dividing size by 8 as image is large
            self.frameCount += 1

def draw(canvas):
    portal.update(canvas)

portal = PortalFinishLine((500, 100), 'adfsda')
frame = simplegui.create_frame("safdasdfsdaf", 599, 700)
frame.set_draw_handler(draw)
frame.start()


