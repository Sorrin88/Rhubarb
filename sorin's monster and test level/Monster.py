try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector

class Monster:

    def __init__(self,level, player, platform):

        self.pos = Vector(platform.p1.x + platform.p2.x / 2, platform.p1.y)
        self.velocity = Vector(0, 0)

        self.spriteSheet = simplegui.load_image('https://i.imgur.com/VLpkuaq.png')
        self.spriteSheetWidth = 348
        self.spriteSheetHeight = 552
        self.columns = 3
        self.rows = 6
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

        self.platform = platform

        self.radius = self.spriteSheetHeight / 2

    def collide(self):
        #if collide then health --
         #if health = 0, then die
        pass

    def isColliding(self,player):
        r1 = self.frameHeight/2
        r0 = player.frameHeight/2
        x1 = self.pos.x
        x0 = player.pos.x
        y1 = self.pos.y
        y0 = player.pos.y

        r2 = player.frameHeight/2
        r3 = self.frameHeight/2
        x2 = player.pos.x
        x3 = self.pos.x
        y2 = player.pos.y
        y3 = self.pos.y
        return (((x0-x1)*2+(y0-y1)*2>=(r0-r1)*2 and (x0-x1)*2+(y0-y1)*2<=(r0+r1)*2)or((x3-x2)*2+(y3-y2)*2>=(r3-r2)*2 and (x3-x2)*2+(y3-y2)*2<=(r3+r2)*2)) and abs(y1-y0) < self.frameHeight/2 #(r0-r1)*2<=(x0-x1)*2+(y0-y1)*2<=(r0+r1)*2
    def hit(self,player):
        playerp1 = Vector(player.pos.x+player.frameWidth/2,player.pos.y+player.frameHeight/2)
        playerp2 = Vector(player.pos.x+player.frameWidth/2,player.pos.y-player.frameHeight/2)
        playerp3 = Vector(player.pos.x-player.frameWidth/2,player.pos.y-player.frameHeight/2)
        playerp4 = Vector(player.pos.x-player.frameWidth/2,player.pos.y+player.frameHeight/2)

        # goatp1 = Vector(self.pos.x+self.frameWidth/2,self.pos.y+self.frameHeight/2)
        # goatp2 = Vector(self.pos.x+self.frameWidth/2,self.pos.y-self.frameHeight/2)
        # goatp3 = Vector(self.pos.x-self.frameWidth/2,self.pos.y-self.frameHeight/2)
        # goatp4 = Vector(self.pos.x-self.frameWidth/2,self.pos.y+self.frameHeight/2)

        goatp1 = Vector(self.pos.x+self.frameWidth/2,self.pos.y)
        goatp2 = Vector(self.pos.x,self.pos.y-self.frameHeight/2)
        goatp3 = Vector(self.pos.x-self.frameWidth/2,self.pos.y)
        goatp4 = Vector(self.pos.x,self.pos.y+self.frameHeight/2)

        unitR = (playerp2-playerp1).normalize()
        unitU =  (playerp3-playerp2).normalize()
        unitL =  (playerp4-playerp3).normalize()
        #return (player.spriteMode == "rAttack" and (self.pos - playerp1).dot(unitR) >= 0 and (self.pos - playerp2).dot(-unitR) >= 0) or ((player.spriteMode == "rAttackUp"or player.spriteMode == "lAttackUp") and (self.pos - playerp2).dot(unitU) >= 0 and (self.pos - playerp3).dot(-unitU) >= 0) or (player.spriteMode == "lAttack" and (self.pos - playerp3).dot(unitL) >= 0 and (self.pos - playerp4).dot(-unitL) >= 0)
        return (player.spriteMode == "rAttack" and (goatp3 - playerp1).dot(unitR) >= 0 and (goatp3 - playerp2).dot(-unitR) >= 0) or ((player.spriteMode == "rAttackUp"or player.spriteMode == "lAttackUp") and (goatp4 - playerp2).dot(unitU) >= 0 and (goatp4 - playerp3).dot(-unitU) >= 0) or (player.spriteMode == "lAttack" and (goatp1 - playerp3).dot(unitL) >= 0 and (goatp1 - playerp4).dot(-unitL) >= 0)


    def imgUpdate(self):
        i = (self.frameIndex[0])
        if self.frameCount % 8 == 0:
            i = (self.frameIndex[0] + 1) % self.columns

        if self.level == 1:
            if self.orientation == 'right':
                j = 0
            if self.orientation == 'left':
                j = 1

        if self.level == 2:
            if self.orientation == 'right':
                j = 2
            if self.orientation == 'left':
                j = 3

        if self.level == 3:
            if self.orientation == 'right':
                j = 4
            if self.orientation == 'left':
                j = 5

        self.frameIndex = (i, j)

    def update(self,canvas):
        canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                              self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), (self.pos.x, self.pos.y), (self.frameWidth, self.frameHeight))

        if self.orientation == 'left':
            self.pos.add(self.velocity)
            if self.pos.x < self.platform.p1.x and self.pos.x < self.platform.p2.x:
                self.orientation = 'right'
            self.imgUpdate()
            self.velocity = Vector(-1, 0).multiply(self.speed)

        elif self.orientation == 'right':
            self.pos.add(self.velocity)
            if self.pos.x > self.platform.p2.x and self.pos.x > self.platform.p1.x:
                self.orientation = 'left'
            self.imgUpdate()
            self.velocity = Vector(1, 0).multiply(self.speed)

        self.frameCount+=1
        # goatp1 = Vector(self.pos.x+self.frameWidth/2,self.pos.y)
        # goatp2 = Vector(self.pos.x,self.pos.y-self.frameHeight/2)
        # goatp3 = Vector(self.pos.x-self.frameWidth/2,self.pos.y)
        # goatp4 = Vector(self.pos.x,self.pos.y+self.frameHeight/2)
        # canvas.draw_circle(goatp1.getP(),3,3,"blue")
        # canvas.draw_circle(goatp2.getP(),3,3,"yellow")
        # canvas.draw_circle(goatp3.getP(),3,3,"purple")
        # canvas.draw_circle(goatp4.getP(),3,3,"yellow")
        # canvas.draw_circle(self.pos.getP(),3,3,"red")
        sub = self.player.pos.copy().subtract2(self.pos)
        if sub.length() <= 50:
            print("GOAT DAMAGE")
