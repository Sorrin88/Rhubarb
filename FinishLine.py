try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class FinishLine:

    def __init__(self, pos, player):

        self.pos = pos
        self.player = player
        self.spriteSheet = simplegui.load_image('https://i.imgur.com/solOsSP.png')
        self.spriteSheetWidth = 3072
        self.spriteSheetHeight = 4096
        self.columns = 3
        self.rows = 4
        self.frameWidth = self.spriteSheetWidth // self.columns
        self.frameHeight = self.spriteSheetHeight // self.rows
        self.frameCentreX = self.frameWidth // 2
        self.frameCentreY = self.frameHeight // 2
        self.frameCount = 0

        self.collided = False

    def collide(self):
        #colllision code....
        # if collided = True:
            #PlatformItem.action()
        pass

    def imgUpdate(self):
        j = self.frameIndex[1]
        i = self.frameIndex[0]
        if self.frameCount % self.spritePlaySpeed == 0:
            i = (self.frameIndex[0] + 1) % self.columns
            if self.frameIndex[1] == self.lastFrameRow and self.frameIndex[0] == 2:
                j = self.topFrameRow
            elif i == 0:
                j = (self.frameIndex[1] + 1) % self.rows
        self.frameIndex = (i, j)

    def update(self, canvas):
        if self.collided == False:
            canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                                 self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                              (self.frameWidth, self.frameHeight), self.pos,
                              (self.frameWidth/8, self.frameHeight/8)) #dividing size by 8 as image is large
            self.frameCount += 1
            self.imgUpdate()