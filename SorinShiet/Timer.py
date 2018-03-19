try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#these must remain global variables because they don't work if i put them inside the class
#nah.. lol :))


class Timer:
    def __init__(self):
        self.frameRate = 60
        self.time = 90
        self.counter = self.time * self.frameRate

    def draw(self, canvas):
        if self.counter % 60 == 0:
            self.time -=1
        self.counter = self.counter - 1
        if self.time < 0:
            time = 0
        minutes = self.time // 60
        seconds = self.time % 60
        timerText = "Time: {0:02}:{1:02}".format(minutes, seconds)
        canvas.draw_text(timerText, (180, 40), 25, 'Black', 'monospace')


