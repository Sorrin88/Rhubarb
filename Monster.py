try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector

class Monster:

    def __init__(self, pos, xVel, yVel, difficulty, level):

        self.pos = pos

        self.spriteSheet = simplegui.load_image('https://i.imgur.com/upaJYsv.png')
        self.spriteSheetWidth = 384
        self.spriteSheetHeight = 1152

        self.xVel = xVel
        self.yVel = yVel

        self.columns = 3
        self.rows = 9

        self.frameWidth = self.spriteSheetWidth // self.columns
        self.frameHeight = self.spriteSheetHeight // self.rows
        self.frameCentreX = self.frameWidth // 2
        self.frameCentreY = self.frameHeight // 2
        self.frameIndex = (0, 0)
        self.frameCount = 1
        self.orientation = 'right'
        self.difficulty = difficulty
        self.level = level

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

        self.velocity = Vector(self.xVel, self.yVel)

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
                j = 4;
            if self.orientation == 'left':
                j = 5;

        if self.level == 3:
            if self.orientation == 'right':
                j = 7;
            if self.orientation == 'left':
                j = 8;

        self.frameIndex = (i, j)

    def update(self,canvas):
        canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                              self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), self.pos.getP(), (self.frameWidth, self.frameHeight))

        if self.orientation == 'left':
            self.pos.add(self.velocity)
            if self.pos.getPx() <= 100:
                self.orientation = 'right'
            self.imgUpdate()
            self.velocity = Vector(-1, 0).multiply(self.speed)
            self.frameCount+=1



        if self.orientation == 'right':
            self.pos.add(self.velocity)
            if self.pos.getPx() >= 400:
                self.orientation = 'left'
            self.imgUpdate()
            self.velocity = Vector(1., 0).multiply(self.speed)
            self.frameCount+=1
            print(self.pos)


