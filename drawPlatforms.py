from Vector import *
import random
from Platform2 import *
class drawPlatforms:
    def __init__(self,difficulty,numberOfPlatforms):
        if difficulty == "easy":
            self.difficulty = 1
        elif difficulty == "medium":
            self.difficulty = 1.5
        else:
            self.difficulty = 2


        self.DISTANCE = 200
        self.coords = []
        self.platform = 1
        self.yVal = 50
        self.frameCount = 0
        self.numberOfPlatforms = numberOfPlatforms

    def draw(self, canvas):
        platform = Platform2(self.yVal)
        self.coords.append(platform)
        if self.platform == 1:
            self.drawLines(canvas)
        elif self.platform < self.numberOfPlatforms:
            if abs(self.coords[self.platform-2].getx1() - abs(self.coords[self.platform-2].getx2()) > self.DISTANCE*self.difficulty or
                   abs(self.coords[self.platform - 2].getx2() - abs(self.coords[self.platform - 2].getx1()) > self.DISTANCE * self.difficulty)):
                pass
            else:
                print("removed")
                self.platform -= 1
                self.draw(canvas)
        else:
            self.coords.pop()
        self.drawLines(canvas)
        if self.platform < self.numberOfPlatforms:
            self.platform += 1

    def drawLines(self, canvas):
        for i in range(self.platform - 1):
            #print(self.coords)
            y = (i + 1) * self.yVal
            canvas.draw_line(self.coords[i].getp1().getP(),self.coords[i].getp2().getP(), 4, "red")
            #print(self.platform)
            # self.frameCount+=1
            # if self.frameCount % 30 == 0:
            #     self.yVal +=1