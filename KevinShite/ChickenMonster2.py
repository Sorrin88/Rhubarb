try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector

from Monster import Monster

class ChickenMonster2(Monster):

    def __init__(self, level, player):

        #Monster.__init__(self, level, player)
        #other attributes etc inherited from Monster
        self.pos = Vector(500, 0)

        self.columns = 2
        self.rows = 6
        self.spriteSheet = simplegui.load_image('https://i.imgur.com/OFzdNYI.png')
        self.spriteSheetWidth = 256
        self.spriteSheetHeight = 768
        self.acc = 1
        self.frameWidth = self.spriteSheetWidth // self.columns
        self.frameHeight = self.spriteSheetHeight // self.rows
        self.frameCentreX = self.frameWidth // 2
        self.frameCentreY = self.frameHeight // 2
        self.frameIndex = (0,0)
        self.frameCount = 0
        self.orientation = 'right'

        self.level = level

        self.health = level
        self.speed = level

        self.player = player


#override Monster's collide method

#Override Monster's

    def update(self,canvas):
        canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                              self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), self.pos.getP(), (self.frameWidth, self.frameHeight))

        sub = self.player.pos.copy().subtract(self.pos)

        if sub.length() > 10:
            if self.player.pos.x < self.pos.x:
                self.orientation = 'left'
            else:
                self.orientation = 'right'

        self.imgUpdate()
        self.frameCount += 1
        if sub.length() < 150:
            if self.acc < 1.8: # max acceleration
                self.acc +=0.2
        direction = sub.getNormalized2() * self.acc * self.speed

        direction.multiply(0.9)
        self.pos.add(direction)
