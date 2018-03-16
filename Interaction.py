from Platform2 import *
class Interaction:
    def __init__(self, object,platform):
        self.object = object
        self.platform = platform
        #self.object.colliding = False


    def update(self):
        if (self.platform.distanceTo(self.object.pos) < (self.platform.thickness + self.object.frameHeight/2) and
            self.platform.covers(self.object.pos))and self.object.pos.getP()[1]-self.object.frameHeight/2<self.platform.p1.getP()[1]:
            #self.object.pos = Vector(self.object.pos.getP()[0],self.platform.p1.getP()[1])
            if not self.object.colliding:
                self.object.collide()
                print("-------collided--------")
                self.object.colliding = True
        else:
            #self.inCollision = False
            self.object.colliding = False
        print("POSITION: ", self.object.pos.getP())
        print("Compared to: ", 500 - self.object.frameHeight / 2)
        #if self.object.pos.getP()[1] < 500 - self.object.frameHeight / 2 and not self.object.colliding:
           #self.object.velocity.subtract(Vector(0,self.object.GRAVITY))
        # elif self.colliding:
        #else:
        if self.object.colliding:
            print("clearly still colliding")
            self.object.velocity = Vector(0, 0)
            self.object.pos = Vector(self.object.pos.getP()[0], self.platform.p1.getP()[1]-self.object.frameHeight/2)
