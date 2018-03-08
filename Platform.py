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
        self.DISTANCE = 150
        self.coords = []
        self.platform = 1
    def draw(self,canvas):
        x1 = random.randint(0,500)
        x2 = x1 + random.randint(-500,500)
        self.coords.append((x1,x2))
        #print(self.coords)
        if self.platform == 1:
            # canvas.draw_line((self.coords[self.platform - 1][0], self.platform * 10),
            #                  (self.coords[self.platform - 1][1], self.platform * 10), 4, "red")
            self.drawLines(canvas)
        else:
            if abs(self.coords[self.platform-2][1]  - self.coords[self.platform-1][0]) > self.DISTANCE*self.difficulty or abs(self.coords[self.platform-2][0]  - self.coords[self.platform-1][1]) > self.DISTANCE*self.difficulty:
                #canvas.draw_line((self.coords[self.platform-1][0],self.platform * 10),(self.coords[self.platform-1][1],self.platform * 10),4,"red")
                self.drawLines(canvas)
            else:
                #self.coords.remove(self.platform)
                print("removed")
                self.coords.pop()
                #self.platform -=1
                #self.draw(canvas)

        if self.platform < 5:
            self.platform+=1
    def drawLines(self,canvas):
        for i in range(len(self.coords)):
            y = (i + 1) * 10
            canvas.draw_line((self.coords[i][0],y),
                             (self.coords[i][1], y), 4, "red")
            print(self.platform)