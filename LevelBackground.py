try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class LevelBackground:

    def __init__(self,backgroundImage):

        self.backgroundImage = simplegui.load_image(backgroundImage)
        #^
        #lv1 https://i.imgur.com/Q7tBgIc.png
        #lv2 https://i.imgur.com/QdnOKPM.png
        #lv3 https://i.imgur.com/15DHBtk.png

        self.imgWidth = 500
        self.imgHeight = 1400
        self.position1 = -700
        self.position2 = 700
        self.timer = 0

    def update(self, canvas):

        if self.position1 < self.imgHeight:
            if self.timer % 3 == 0:
                canvas.draw_image(self.backgroundImage, (self.imgWidth / 2, self.imgHeight / 2), (self.imgWidth, self.imgHeight),
                                  (self.imgWidth / 2, self.position1), (self.imgWidth, self.imgHeight))
                self.position1 = self.position1 + 1
                self.timer = self.timer + 1
            else:
                canvas.draw_image(self.backgroundImage, (self.imgWidth / 2, self.imgHeight / 2), (self.imgWidth, self.imgHeight),
                                  (self.imgWidth / 2, self.position1), (self.imgWidth, self.imgHeight))
                self.timer = self.timer + 1
        else:
            canvas.draw_image(self.backgroundImage, (self.imgWidth / 2, self.imgHeight / 2), (self.imgWidth, self.imgHeight),
                              (self.imgWidth / 2, self.position1), (self.imgWidth, self.imgHeight))
            self.position1 = -700

        if self.position2 < self.imgHeight:
            if self.timer % 3 == 0:
                canvas.draw_image(self.backgroundImage, (self.imgWidth / 2, self.imgHeight / 2), (self.imgWidth, self.imgHeight),
                                  (self.imgWidth / 2, self.position2), (self.imgWidth, self.imgHeight))
                self.position2 = self.position2 + 1
                self.timer = self.timer + 1
            else:
                canvas.draw_image(self.backgroundImage, (self.imgWidth / 2, self.imgHeight / 2), (self.imgWidth, self.imgHeight),
                                  (self.imgWidth / 2, self.position2), (self.imgWidth, self.imgHeight))
                self.timer = self.timer + 1
        else:
            canvas.draw_image(self.backgroundImage, (self.imgWidth / 2, self.imgHeight / 2), (self.imgWidth, self.imgHeight),
                              (self.imgWidth / 2, self.position2), (self.imgWidth, self.imgHeight))
            self.position2 = -700

def draw(canvas):
    lv1.update(canvas)

lv1 = LevelBackground('https://i.imgur.com/Q7tBgIc.png')
frame = simplegui.create_frame("level1sky", 500, 700)
frame.set_draw_handler(draw)
frame.start()


