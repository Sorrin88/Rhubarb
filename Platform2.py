from Vector import *
import random
class Platform2:
    def __init__(self,yCoord):
        self.yCoord = yCoord
        self.p1 = Vector(random.randint(0,500),self.yCoord)
        self.p2 = Vector(self.p1.getP()[1] + random.randint(-500, 500), self.yCoord)
        while(self.p1.getP()[0] == self.p2.getP()[0]):
            self.p2 = Vector(self.p1.getP()[1] + random.randint(-500, 500), self.yCoord)
        self.unit = (self.p2 - self.p1).normalize()
        self.normal = self.rotateAnti(self.unit)
        self.thickness = 4
    def rotateAnti(self,v):
        return Vector(-v.y, v.x)
    def distanceTo(self, pos):
        posToA = pos - self.p2
        proj = posToA.dot(self.normal) * self.normal
        return proj.length()
    def covers(self, pos):
        return ((pos - self.p1).dot(self.unit) >= 0 and
                (pos - self.p2).dot(-self.unit) >= 0) and pos.getP()[1]<self.yCoord
    def getp1(self):
        return self.p1
    def getp2(self):
        return self.p2
    def getx1(self):
        return self.p1.getP()[0]
    def getx2(self):
        return self.p2.getP()[0]
    def draw(self,canvas):
        #print("a line: ",self.p1.getP(),self.p2.getP())
        canvas.draw_line(self.p1.getP(),self.p2.getP(),3,"red")