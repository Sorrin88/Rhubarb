from Vector import *
import random
class Platform:
    def __init__(self,difficulty):
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
    def rotateAnti(self,v):
        return Vector(-v.y, v.x)

    def draw(self,canvas):
        x1 = random.randint(0,500)
        x2 = x1 + random.randint(-500,500)
        self.coords.append((x1,x2))
        #print(self.coords)
        print(abs(self.coords[self.platform - 2][1] - self.coords[self.platform - 1][0]))
        print("---------")
        print(self.DISTANCE * self.difficulty)
        print("---------")
        print(abs(self.coords[self.platform - 2][0] - self.coords[self.platform - 1][1]))
        if self.platform == 1:
            # canvas.draw_line((self.coords[self.platform - 1][0], self.platform * 10),
            #                  (self.coords[self.platform - 1][1], self.platform * 10), 4, "red")
            self.drawLines(canvas)
        elif self.platform<9:
            if abs(self.coords[self.platform-2][1]  - self.coords[self.platform-1][0]) > self.DISTANCE*self.difficulty or abs(self.coords[self.platform-2][0]  - self.coords[self.platform-1][1]) > self.DISTANCE*self.difficulty:
                pass#canvas.draw_line((self.coords[self.platform-1][0],self.platform * 10),(self.coords[self.platform-1][1],self.platform * 10),4,"red")
            else:
                #self.coords.remove(self.platform)
                print("removed")
                self.coords.pop()
                #self.coords.remove("Null")
                self.platform -=1
                self.draw(canvas)
        else:
            self.coords.pop()
        self.drawLines(canvas)
        if self.platform < 9:
            self.platform+=1
    def drawLines(self,canvas):
        for i in range(self.platform-1):
            print(self.coords)
            y = (i + 1) * self.yVal
            canvas.draw_line((self.coords[i][0], y),
                             (self.coords[i][1], y), 4, "red")
            print(self.platform)
            # self.frameCount+=1
            # if self.frameCount % 30 == 0:
            #     self.yVal +=1