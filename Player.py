try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from Vector import *


class Player:
    def __init__(self, startingpos, spritesheet, up, left, down, right, lifepoints):
            self.pos = startingpos
            self.spriteSheet = spritesheet
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

    def update(self,canvas):
        if self.moveRight:
            self.velocity.add(Vector(0,5))
        if self.moveLeft:
            self.velocity.add(Vector(0,-5))
        if self.moveUp:
            self.velocity.add(Vector(-5,0))
        if self.moveDown:
            self.velocity.add(Vector(5,0))
        self.pos.add(self.velocity)
        canvas.draw_circle(self.pos,1,1,'red')