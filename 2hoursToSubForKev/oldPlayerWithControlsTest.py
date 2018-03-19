try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import Vector


class Player:

    def __init__(self, startingpos):
        self.GRAVITY = -9.81
        self.pos = startingpos
        self.spriteSheet = simplegui.load_image('https://i.imgur.com/k1U4E3J.png')
        self.up = 'w'
        self.up2 = 'space'
        self.left = 'a'
        self.right = 'd'
        self.keyAttackUp = 'up'
        self.keyAttackLeft = 'left'
        self.keyAttackRight = 'right'
        self.lifePoints = 3
        self.moveRight = False
        self.moveLeft = False
        self.moveUp = False
        self.attackUp = False
        self.attackLeft = False
        self.attackRight = False
        self.colliding = True

        self.xVel = 0.0
        self.yVel = 0.0
        self.velocity = Vector(self.xVel, self.yVel)

        self.WIDTH = 672
        self.HEIGHT = 1680
        self.radius = self.HEIGHT / 2
        self.COLUMNS = 4
        self.ROWS = 10
        self.currentRow = 3

        self.frameWidth = self.WIDTH // self.COLUMNS
        self.frameHeight = self.HEIGHT // self.ROWS
        self.frameCentreX = self.frameWidth / 2
        self.frameCentreY = self.frameHeight / 2
        self.frameIndex = (0,0)
        self.frameCount = 0
        self.spriteMode = 'rStand'

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

    def collide(self):
        pass

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
        if self.pos.getP()[1] < 500 - self.frameHeight / 2:
            self.velocity = self.velocity.subtract(Vector(0, self.GRAVITY))
        else:
            self.velocity = Vector(0, 0)
            self.pos = Vector(self.pos.getP()[0], 500 - self.frameHeight / 2)


    def getCoordinates(self):
        return self.pos


    def update(self, canvas):
        self.addGravity()
        if self.moveUp and self.velocity.getP()[1] < 9.4:
            self.velocity.add(Vector(0, -9.4))
        if self.moveRight and self.velocity.getP()[0] < 9:
            self.velocity.add(Vector(9, 0))
        if self.moveLeft and self.velocity.getP()[0] > -9:
            self.velocity.add(Vector(-9, 0))
        self.pos.add(self.velocity)

        if self.pos.getP()[0] > 1000 - self.frameHeight / 2:
            self.pos = Vector(0, self.pos.getP()[1])
        elif self.pos.getP()[0] < 0:
            self.pos = Vector(1000 - self.frameHeight / 2, self.pos.getP()[1])

        canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                             self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), self.pos.getP(), (self.frameWidth, self.frameHeight))
        self.imgUpdate()
        self.frameCount += 1

player1 = Player(Vector(100,100))

def draw(canvas):
    player1.update(canvas)
def keyUp(key):
    player1.keyUp(key)
def keyDown(key):
    player1.keyDown(key)

frame = simplegui.create_frame("aseff",1000,500)
frame.set_draw_handler(draw)
frame.set_keyup_handler(keyUp)
frame.set_keydown_handler(keyDown)
frame.start()
