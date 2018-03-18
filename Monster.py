try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector

class Monster:

    def __init__(self, pos, level, player):

        self.pos = pos
        self.velocity = Vector(0, 0)

        self.spriteSheet = simplegui.load_image('https://i.imgur.com/LROJe4y.png')
        self.spriteSheetWidth = 384
        self.spriteSheetHeight = 768
        self.columns = 3
        self.rows = 6
        self.frameWidth = self.spriteSheetWidth // self.columns
        self.frameHeight = self.spriteSheetHeight // self.rows
        self.frameCentreX = self.frameWidth // 2
        self.frameCentreY = self.frameHeight // 2
        self.frameIndex = (0,0)
        self.frameCount = 0
        self.orientation = 'right'

        level = level

        self.health = level
        self.speed = level

        self.player = player

        self.radius = self.spriteSheetHeight / 2

    def collide(self):
        #if collide then health --
         #if health = 0, then die
        pass

    def imgUpdate(self):
        i = (self.frameIndex[0])
        if self.frameCount % 8 == 0:
            i = (self.frameIndex[0] + 1) % self.columns

        if self.level == 1:
            if self.orientation == 'right':
                j = 0;
            if self.orientation == 'left':
                j = 1;

        if self.level == 2:
            if self.orientation == 'right':
                j = 2;
            if self.orientation == 'left':
                j = 3;

        if self.level == 3:
            if self.orientation == 'right':
                j = 4;
            if self.orientation == 'left':
                j = 5;

        self.frameIndex = (i, j)

    def update(self,canvas):
        canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                              self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), self.pos.getP(), (self.frameWidth, self.frameHeight))

        if self.orientation == 'left':
            self.pos.add(self.velocity)
            if self.pos.x <= 100:
                self.orientation = 'right'
            self.imgUpdate()
            self.velocity = Vector(-1, 0).multiply(self.speed)

        elif self.orientation == 'right':
            self.pos.add(self.velocity)
            if self.pos.x >= 300:
                self.orientation = 'left'
            self.imgUpdate()
            self.velocity = Vector(1, 0).multiply(self.speed)

        self.frameCount+=1

        sub = self.player.pos.copy().subtract(self.pos)
        if sub.length() <= 50:
            print("GOAT DAMAGE")


