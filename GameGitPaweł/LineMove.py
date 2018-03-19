try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
from Vector import Vector

class LineMove :

    def __init__(self, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2

        self.xVel = random.randint(,250)
        self.yVel = random.randint(1,500)
        self.velocity = Vector(self.xVel, self.yVel)

    def collide(self):
        pass

    def update(self,canvas):
            self.pos1.add(self.velocity)
            self.pos2.add(self.velocity)
            print(self.pos1.getP())
            print(self.pos1.getP())
            canvas.draw_line((self.pos1.getP()), (self.pos2.getP()), 5,'Red')
            self.velocity = Vector(0, +1)


