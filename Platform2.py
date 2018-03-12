from Vector import *
import random
class Platform2:
    def __init__(self,yCoord):
        self.yCoord = yCoord
        self.p1 = Vector(random.randint(0,500),self.yCoord)
        self.p2 = Vector(self.p1.getP()[1] + random.randint(-500,500),self.yCoord)
        self.unit = Vector(self.p1.subtract(self.p2).normalize())
        self.normal = self.rotateAnti(self.unit)
    def rotateAnti(self,v):
        return Vector(-v.getP()[1], v.getP()[0])
    def distanceTo(self, pos):
        posToA = pos - self.p1
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