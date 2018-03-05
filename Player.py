try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import *


class Player:

    def __init__(self, startingpos, spritesheet, up, left, down, right, lifepoints):
            self.GRAVITY = -9.81
            self.pos = startingpos
            self.spriteSheet = simplegui.load_image(spritesheet)
            self.up = up
            self.left = left
            self.down = down
            self.right = right
            self.lifePoints = lifepoints
            self.moveRight = False
            self.moveLeft = False
            self.moveUp = False
            self.moveDown = False
            self.xVel = 0.0
            self.yVel = 0.0
            self.velocity = Vector(self.xVel,self.yVel)

            self.WIDTH = 256
            self.HEIGHT = 256
            self.COLUMNS = 2
            self.ROWS = 2
            self.frameWidth = self.WIDTH//self.COLUMNS
            self.frameHeight = self.HEIGHT//self.ROWS
            self.frameCentreX = self.frameWidth / 2
            self.frameCentreY = self.frameHeight / 2
            self.frameIndex = [self.COLUMNS, self.ROWS]
            self.frameCount = 0
    def keyDown(self, key):
        if key == simplegui.KEY_MAP[self.right]:
            self.moveRight = True
            self.moveLeft = False

        if key == simplegui.KEY_MAP[self.left]:
            self.moveLeft = True
            self.moveRight = False

        if key == simplegui.KEY_MAP[self.up]:
            self.moveUp = True
            self.moveDown = False

        if key == simplegui.KEY_MAP[self.down]:
            self.moveDown = True
            self.moveUp = False
    def keyUp(self, key):
        if key == simplegui.KEY_MAP[self.right]:
            self.moveRight = False
        if key == simplegui.KEY_MAP[self.left]:
            self.moveLeft = False
        if key == simplegui.KEY_MAP[self.down]:
            self.moveDown = False
        if key == simplegui.KEY_MAP[self.up]:
            self.moveUp = False
    def collide(self):
        pass

    def imgUpdate(self):
        if self.frameCount % 15 == 0:
            self.frameIndex[0] = (self.frameIndex[0] + 1) % self.COLUMNS
            if self.frameIndex[0] == 0:
                self.frameIndex[1] = (self.frameIndex[1] + 1) % self.ROWS


    def update(self,canvas):

        if self.moveUp:
            self.velocity.add(Vector(0,-10))
        if self.moveDown:
            self.velocity.add(Vector(0,10))
        if self.moveRight:
            self.velocity.add(Vector(10,0))
        if self.moveLeft:
            self.velocity.add(Vector(-10,0))
        self.pos.add(self.velocity)
        print(self.pos.getP())
        canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX, self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), self.pos.getP(), (self.frameWidth, self.frameHeight))
        self.imgUpdate()
        #canvas.draw_circle(self.pos.getP(), 50, 10, 'red')
        # if self.pos.getP()[1] <= 500:
        #     self.velocity.add(Vector(0,self.GRAVITY))
        # else:
        self.velocity = Vector(0, 0)
        self.frameCount+=1

