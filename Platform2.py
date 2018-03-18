from Vector import *
import random
class Platform2:
    def __init__(self,yCoord):
        self.yCoord = yCoord
        self.p1 = Vector(random.randint(0,500),self.yCoord)
        self.p2 = Vector(self.p1.x + random.randint(-500, 500), self.yCoord)
        while(self.p1.x == self.p2.x) or abs(self.p2.x-self.p1.x)<=200 or abs(self.p2.x-self.p1.x)>=250:
            self.p2 = Vector(self.p1.x + random.randint(-500, 500), self.yCoord)
        if self.p2.x >=500:
            self.p2.x -=100
            self.p1.x -= 100
        if self.p1.x <=0:
            self.p1.x +=100
            self.p2.x += 100
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
                (pos - self.p2).dot(-self.unit) >= 0)
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