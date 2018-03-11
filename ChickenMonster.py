try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import math

from Vector import Vector

from Monster import Monster

class ChickenMonster(Monster):

    def __init__(self, pos:Vector, xVel, yVel, difficulty, level, player):
        super().__init__(pos, xVel, yVel, difficulty, level)

        self.pos = pos
        self.xVel = xVel
        self.yVel = yVel

        self.spriteSheet = simplegui.load_image('https://i.imgur.com/CqHIE2B.png')
        self.spriteSheetWidth = 256
        self.spriteSheetHeight = 1152

        self.frameIndex = (0, 0)
        self.columns = 2
        self.rows = 9

        self.frameWidth = self.spriteSheetWidth // self.columns
        self.frameHeight = self.spriteSheetHeight // self.rows
        self.frameCentreX = self.frameWidth // 2
        self.frameCentreY = self.frameHeight // 2
        self.frameIndex = (0, 0)
        self.frameCount = 1
        self.orientation = 'right'
        self.difficulty = difficulty
        self.level = 1

        if difficulty == 'easy':
            difficulty = 1
        elif difficulty =='medium':
            difficulty = 2
        elif difficulty == 'hard':
            difficulty = 3
        else:
            print("you can't spell")
            difficulty = 50

        self.health = difficulty
        self.speed = difficulty

        self.playerCoords = player.getCoordinates()

    def collide(self):
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
                j = 3;
            if self.orientation == 'left':
                j = 4;

        if self.level == 3:
            if self.orientation == 'right':
                j = 6;
            if self.orientation == 'left':
                j = 7;

        self.frameIndex = (i, j)

    def update(self,canvas):

        canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                              self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), self.pos.getP(), (self.frameWidth, self.frameHeight))

        subInte = self.pos.inte()
        sub = subInte.subtract(self.playerCoords)# round before normalise....
        direction = sub.getNormalized()*4
        self.pos.add(direction)
        self.imgUpdate()
        self.frameCount +=1

        # self.pos.add(self.velocity)
        # print(self.pos.getP())
        # self.imgUpdate()
        # self.velocity = self.playerCoords
        # self.frameCount+=1



        #get the position ot both of the sprites
        #player sprite - enemy sprite
        # #normalize this