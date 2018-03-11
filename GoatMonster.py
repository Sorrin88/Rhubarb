try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector

from Monster import Monster

class GoatMonster(Monster):

    def __init__(self, pos, xVel, yVel, difficulty, level):
        super()
        self.pos = pos

        self.xVel = xVel
        self.yVel = yVel
        self.width = 118
        self.height = 118

        self.spriteSheet = simplegui.load_image('https://i.imgur.com/upaJYsv.png')
        self.spriteSheetWidth = 384
        self.spriteSheetHeight = 1152

        self.frameWidth = 118
        self.frameHeight = 118
        self.frameIndex = (0, 0)
        self.columns = 3
        self.rows = 9

        self.difficulty = difficulty

        if difficulty == 'easy':
            difficulty = 1
        elif difficulty =='medium':
            difficulty = 2
        else:
            difficulty = 3

        self.health = difficulty
        self.speed = difficulty

        self.velocity = Vector(self.xVel, self.yVel)

        self.level = level




    def collide(self):
        pass

    def imgUpdate(self):
        if self.frameCount % 15 == 0:
            self.frameIndex[0] = (self.frameIndex[0] + 1) % self.COLUMNS

        if self.level == 1:
            if self.orientation == 'right':
                self.frameIndex[1] = 0;
            if self.orientation == 'left':
                self.frameIndex[1] = 1;

        if self.level == 2:
            if self.orientation == 'right':
                self.frameIndex[1] = 3;
            if self.orientation == 'left':
                self.frameIndex[1] = 4;

        if self.level == 3:
            if self.orientation == 'right':
                self.frameIndex[1] = 6;
            if self.orientation == 'left':
                self.frameIndex[1] = 7;


    def update(self,canvas):

        canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                              self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), self.pos.getP(), (self.frameWidth, self.frameHeight))

        if self.orientation == 'left':
            self.pos.add(self.velocity)
            print(self.pos.getP())
            self.imgUpdate()
            self.velocity = Vector(2, 0)
            self.frameCount+=1
            if self.pos == Vector(0, 0):
                self.orientation = 'right'

        if self.orientation == 'right':
            self.pos.add(self.velocity)
            print(self.pos.getP())
            self.imgUpdate()
            self.velocity = Vector(-2, 0)
            self.frameCount+=1
            if self.pos == Vector(200, 0):
                self.orientation = 'left'