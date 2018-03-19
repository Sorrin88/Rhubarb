try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Player import Player

class LifeBar:

    def __init__(self, player):

        self.pos = 430, 30 #can change position of life/healthbar later
        self.player = player

        self.spriteSheet = simplegui.load_image('https://i.imgur.com/XRHoM0s.png')
        self.frameIndex = (3,0)
        self.spriteSheetWidth = 384
        self.spriteSheetHeight = 128
        self.columns = 3
        self.rows = 1
        self.frameWidth = self.spriteSheetWidth // self.columns
        self.frameHeight = self.spriteSheetHeight // self.rows
        self.frameCentreX = self.frameWidth // 2
        self.frameCentreY = self.frameHeight // 2
        self.frameIndex = (0, 0)

    def update(self, canvas):

        if self.player.alive == True:
            
            if self.player.lives == 3: # add player here
                self.frameIndex = (0,0)
            elif self.player.lives == 2:
                self.frameIndex = (0, 1)
            elif self.player.lives == 1:
                self.frameIndex = (0,2)

                canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                                     self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                                  (self.frameWidth, self.frameHeight), self.pos,
                                  (self.frameWidth, self.frameHeight))

def draw(canvas):
    life.update(canvas)

life = LifeBar('adfsda')
frame = simplegui.create_frame("safdasdfsdaf", 500, 700)
frame.set_draw_handler(draw)
frame.start()


