try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import *


class Player2:

    def __init__(self, startingpos, spritesheet, width, height, rows, columns, up, left, down, right,
                 keyAttackUp, keyAttackLeft, keyAttackRight, scoreCount, lifePoints):
        self.GRAVITY = -9.81
        self.pos = startingpos
        self.spriteSheet = simplegui.load_image(spritesheet)
        self.up = up
        self.left = left
        self.down = down
        self.right = right
        self.keyAttackUp = keyAttackUp
        self.keyAttackLeft = keyAttackLeft
        self.keyAttackRight = keyAttackRight
        self.up2 = 'space'
        #self.attack = attack
        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.attacking = False
        self.moveDown = False
        self.attackUp = False
        self.attackLeft = False
        self.attackRight = False
        self.velocity = Vector(0, 0)
        self.colliding = False
        # Sprite
        self.WIDTH = width
        self.HEIGHT = height
        self.COLUMNS = columns
        self.ROWS = rows
        self.currentRow = 3
        self.frameWidth = self.WIDTH // self.COLUMNS
        self.frameHeight = self.HEIGHT // self.ROWS
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2
        self.frameIndex = [self.COLUMNS, self.ROWS]
        self.frameCount = 0
        self.spriteMode = 'rStand'
        # /sprite

        self.scoreCount = scoreCount
        self.lifePoints = lifePoints

    def keyDown(self, key):

        if key == simplegui.KEY_MAP[self.right]:
            self.moveRight = True
            self.moveLeft = False
            self.spriteMode = 'rRun'

        if key == simplegui.KEY_MAP[self.left]:
            self.moveLeft = True
            self.moveRight = False
            self.spriteMode = 'lRun'

        if key == simplegui.KEY_MAP[self.up] or key == simplegui.KEY_MAP[self.up2]:
            self.moveUp = True
            if self.spriteMode == 'lRun' or self.spriteMode == 'lStand' or self.spriteMode == 'lAttack':
                self.spriteMode = 'lJump'
            elif self.spriteMode == 'rRun' or self.spriteMode == 'rStand' or self.spriteMode == 'rAttack':
                self.spriteMode = 'rJump'

        if key == simplegui.KEY_MAP[self.keyAttackUp]:

            self.attackUp = True
            if self.spriteMode == 'lRun' or self.spriteMode == 'lStand' or self.spriteMode == 'lJump':
                self.spriteMode = 'lAttackUp'
            elif self.spriteMode == 'rRun' or self.spriteMode == 'rStand' or self.spriteMode == 'rJump':
                self.spriteMode = 'rAttackUp'

        if key == simplegui.KEY_MAP[self.keyAttackLeft]:
            self.attackLeft = True
            self.moveRight = False
            self.spriteMode = 'lAttack'

        if key == simplegui.KEY_MAP[self.keyAttackRight]:
            self.attackRight = True
            self.moveLeft = False
            self.spriteMode = 'rAttack'

    def keyUp(self, key):

        if key == simplegui.KEY_MAP[self.right]:
            self.moveLeft = False
            self.moveRight = False
            if self.spriteMode != 'rAttack':
                self.spriteMode = 'rStand'

        if key == simplegui.KEY_MAP[self.left]:
            self.moveLeft = False
            self.moveRight = False
            if self.spriteMode != 'lAttack':
                self.spriteMode = 'lStand'

        if key == simplegui.KEY_MAP[self.up] or key == simplegui.KEY_MAP[self.up2]:
            self.moveUp = False
            if self.spriteMode == 'lJump' and self.moveLeft == True:
                self.spriteMode = 'lRun'
            elif self.spriteMode == 'rJump' and self.moveRight == True:
                self.spriteMode = 'rRun'
            elif self.spriteMode == 'lJump':
                self.spriteMode = 'lStand'
            elif self.spriteMode == 'rJump':
                self.spriteMode = 'rStand'

        if key == simplegui.KEY_MAP[self.keyAttackUp]:
            self.attackUp = False
            if self.spriteMode == 'lAttackUp' and self.moveLeft == True:
                self.spriteMode = 'lRun'
            elif self.spriteMode == 'rAttackUp' and self.moveRight == True:
                self.spriteMode = 'rRun'
            elif self.spriteMode == 'lAttackUp':
                self.spriteMode = 'lStand'
            elif self.spriteMode == 'rAttackUp':
                self.spriteMode = 'rStand'

        if key == simplegui.KEY_MAP[self.keyAttackLeft]:
            self.attackLeft = False
            if self.moveLeft == True:
                self.spriteMode = 'lRun'
            else:
                self.spriteMode = 'lStand'

        if key == simplegui.KEY_MAP[self.keyAttackRight]:
            self.attackRight = False
            if self.moveRight == True:
                self.spriteMode = 'rRun'
            else:
                self.spriteMode = 'rStand'

    def imgUpdate(self):

        if self.spriteMode == 'rStand':
            self.frameIndex = (0, 2)
        elif self.spriteMode == 'lStand':
            self.frameIndex = (0, 3)
        elif self.spriteMode == 'rJump':
            self.frameIndex = (0, 4)
        elif self.spriteMode == 'lJump':
            self.frameIndex = (0, 5)
        else:
            if self.spriteMode == 'rRun':
                self.currentRow = 0
            elif self.spriteMode == 'lRun':
                self.currentRow = 1
            elif self.spriteMode == 'rAttack':
                self.currentRow = 6
            elif self.spriteMode == 'lAttack':
                self.currentRow = 7
            elif self.spriteMode == 'rAttackUp':
                self.currentRow = 8
            elif self.spriteMode == 'lAttackUp':
                self.currentRow = 9

            i = self.frameIndex[0]
            if self.frameCount % 8 == 0:
                i = (self.frameIndex[0] + 1) % self.COLUMNS
            self.frameIndex = (i, self.currentRow)

    def addGravity(self):
        # if self.pos.getP()[1] < 500-self.frameHeight/2 and not self.colliding:
        #     self.velocity.subtract(Vector(0,self.GRAVITY))
        #    # print(self.velocity.getP())
        # elif self.colliding:
        #     self.velocity = Vector(0,0)
        #     self.pos =  Vector(self.pos.getP()[0],460-self.frameHeight/2)
        # else:
        #     #self.velocity = self.velocity.multiplyVectors(Vector(0,0))
        #     self.velocity = Vector(0,0)
        # #     self.pos =  Vector(self.pos.getP()[0],500-self.frameHeight/2)
        if not self.colliding and self.pos.getP()[1] < 700 - self.frameHeight / 2:
            self.velocity.subtract(Vector(0, self.GRAVITY))
        print("-----------")
        #
        # if self.pos.getP()[1] < 500-self.frameHeight/2:
        #     self.velocity.subtract(Vector(0,self.GRAVITY))
        # #elif self.colliding:
        # else:
        #     self.velocity = Vector(0,0)
        #     self.pos =  Vector(self.pos.getP()[0],500-self.frameHeight/2)

        # else:
        #     self.velocity = self.velocity.multiplyVectors(Vector(0, 0))
        # self.pos = Vector(self.pos.getP()[0], 460 - self.frameHeight / 2)

    def getCoordinates(self):
        return self.pos
    def collide(self):
        self.velocity.multiplyVectors(Vector(1,0))
    def update(self, canvas):
        # print(self.velocity.getP()[1])
        print("velocity:", self.velocity.getP())
        if self.moveUp and self.velocity.getP()[1] > -9.4:
            # print(self.velocity.getP()[1])
            self.colliding = False
            print("-----------------------------------Moving up---------------------------")
            self.velocity.add(Vector(0, -9.4))
        # if self.moveDown and self.pos.getP()[1] < 500-self.frameHeight/2:
        #         self.velocity.add(Vector(0,9))
        if self.moveDown:
            self.colliding = False
        if self.moveRight and self.velocity.getP()[0] < 6:
            self.velocity.add(Vector(6, 0))
        if self.moveLeft and self.velocity.getP()[0] > -6:
            self.velocity.add(Vector(-6, 0))
        if self.attacking:
            print("boom")

        #################################

        #################################
        if self.pos.getP()[0] > 500 + self.frameHeight / 2:
            self.pos = Vector(0, self.pos.getP()[1])
        elif self.pos.getP()[0] < 0:
            self.pos = Vector(500 - self.frameHeight / 2, self.pos.getP()[1])
        # print(self.pos.getP())
        # print(500-self.frameHeight/2)
        canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                             self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), (self.pos.x, self.pos.y + 23), (self.frameWidth/2, self.frameHeight/2))
        self.imgUpdate()

        self.pos.add(self.velocity)
        self.addGravity()
        self.frameCount += 1
        # self.velocity = Vector(0,0)
        # self.colliding = False
