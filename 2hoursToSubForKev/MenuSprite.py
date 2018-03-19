try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui


class MenuSprite:

    def __init__(self, pos):
        self.pos = pos
        self.spriteSheet = simplegui.load_image('https://i.imgur.com/alQYd7X.png')
        self.spriteSheetWidth = 256
        self.spriteSheetHeight = 256
        self.columns = 2
        self.rows = 2
        self.frameWidth = self.spriteSheetWidth // self.columns
        self.frameHeight = self.spriteSheetHeight // self.rows
        self.frameCentreX = self.frameWidth // 2
        self.frameCentreY = self.frameHeight // 2
        self.frameIndex = (0, 0)
        self.frameCount = 0

    def imgUpdate(self):
        i = (self.frameIndex[0])

        if self.frameCount % 6 == 0:
            i = (self.frameIndex[0] + 1) % self.columns
            if i == 0:
                j = (self.frameIndex[1] + 1) % self.rows
            else:
                j = self.frameIndex[1]

            self.frameIndex = (i, j)

    def draw(self, canvas):
        canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                             self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), self.pos, (self.frameWidth, self.frameHeight))
        self.imgUpdate()
        self.frameCount += 1
