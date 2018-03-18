try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector

from Monster import Monster

class ChickenMonster2(Monster):

    def __init__(self, pos:Vector, level, player):

        Monster.__init__(self, pos, level, player)
        #other attributes etc inherited from Monster

        self.columns = 2
        self.spriteSheet = simplegui.load_image('https://i.imgur.com/OFzdNYI.png')
        self.spriteSheetWidth = 256
        self.acc = 1

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
        else:
            print("DAMAGE")

        self.imgUpdate()
        self.frameCount += 1
        if sub.length() < 150:
            if self.acc < 1.8: # max acceleration
                self.acc +=0.2
        direction = sub.getNormalized() * self.acc * self.speed

        direction.multiply(0.9)
        self.pos.add(direction)
