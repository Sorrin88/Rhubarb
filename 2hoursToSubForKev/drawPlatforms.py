from Vector import *
import random
from Platform2 import *
import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
class drawPlatforms:
    def __init__(self,difficulty,numberOfPlatforms):
        if difficulty == "easy":
            self.difficulty = 1
        elif difficulty == "medium":
            self.difficulty = 1.5
        else:
            self.difficulty = 2

        self.DISTANCE = 100
        self.coords = []
        self.platform = 1
        self.yVal = 100
        self.frameCount = 0
        self.numberOfPlatforms = numberOfPlatforms
        self.createPlatforms()

    def createPlatforms(self):
        if self.platform <= self.numberOfPlatforms:
            temp = Platform2(self.yVal * self.platform)
            #print("made platform: ",self.platform)
            self.coords.append(temp)
            if self.platform > 1:
                if not (abs(self.coords[self.platform-1].getx1() - self.coords[self.platform-2].getx1()) > self.DISTANCE*self.difficulty or abs(self.coords[self.platform - 1].getx2() - self.coords[self.platform - 2].getx2()) > self.DISTANCE * self.difficulty):
                    #print("removed because: ",abs(self.coords[self.platform-2].getx1() - self.coords[self.platform-2].getx1()) , " or: ",abs(self.coords[self.platform - 2].getx2() - self.coords[self.platform - 2].getx2())  )
                    self.coords.pop()
                    self.platform-=1
        if self.platform <= self.numberOfPlatforms:
            self.platform+=1
            self.createPlatforms()

    def draw(self, canvas):

        self.drawLines(canvas)

    def drawLines(self, canvas):
        for i in range(self.platform-1):
            #print(self.coords)
            #y = (i + 1) * self.yVal
            #canvas.draw_line(self.coords[i].getp1().getP(),self.coords[i].getp2().getP(), self.coords[i].thickness, "red")
            img = simplegui.load_image("https://i.imgur.com/29YK6bh.png")
            #self.coords[i].yCoord +=1
            canvas.draw_image(img,(128/2,32/2),(128,32),(self.coords[i].getp1().getP()[0]+(self.coords[i].getp2().getP()[0]-self.coords[i].getp1().getP()[0])/2,self.coords[i].getp1().getP()[1]),(abs(self.coords[i].getp2().getP()[0] - self.coords[i].getp1().getP()[0]),self.coords[i].thickness*16))
            #print(i)
            #print(self.coords)
            #print(self.coords[i].getp1().getP(),self.coords[i].getp2().getP() )
            #print(self.platform)
            # self.frameCount+=1
            # if self.frameCount % 30 == 0:
            #     self.yVal +=1
    def getNumberOfPlatforms(self):
        return self.numberOfPlatforms
    def getCoords(self):
        return self.coords