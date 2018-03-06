try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import *


class Player:

    def __init__(self, startingpos, spritesheet,width,height,rows,columns, up, left, down, right, lifepoints):
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
            #Sprite
            self.WIDTH = width
            self.HEIGHT = height
            self.COLUMNS = columns
            self.ROWS = rows
            self.frameWidth = self.WIDTH//self.COLUMNS
            self.frameHeight = self.HEIGHT//self.ROWS
            self.frameCentreX = self.frameWidth / 2
            self.frameCentreY = self.frameHeight / 2
            self.frameIndex = [self.COLUMNS, self.ROWS]
            self.frameCount = 0
            #/sprite
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


    def addGravity(self):
        if self.pos.getP()[1] < 500-self.frameHeight/2:
            self.velocity = self.velocity.subtract(Vector(0,self.GRAVITY))
           # print(self.velocity.getP())
        else:
            #self.velocity = self.velocity.multiplyVectors(Vector(0,0))
            self.velocity = Vector(0,0)
            self.pos =  Vector(self.pos.getP()[0],500-self.frameHeight/2)



    def update(self,canvas):
        if self.moveUp and self.velocity.getP()[1] < 10:
                print(self.pos.getP()[1])
                self.velocity.add(Vector(0,-10))
        if self.moveDown and self.pos.getP()[1] < 500-self.frameHeight/2:
                self.velocity.add(Vector(0,10))
        if self.moveRight:
            self.velocity.add(Vector(10,0))
        if self.moveLeft:
            self.velocity.add(Vector(-10,0))
        self.pos.add(self.velocity)
        #print(self.pos.getP())
        canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX, self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), self.pos.getP(), (self.frameWidth, self.frameHeight))
        self.imgUpdate()
        self.addGravity()
        self.frameCount+=1

