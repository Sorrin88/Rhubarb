try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

#these must remain global variables because they don't work if i put them inside the class
frameRate = 60
time = 90
counter = time * frameRate

class Timer:
    def __init__(self, font_size, font_colour):
        self.font_size = font_size
        self.font_colour = font_colour
        self.font = 'monospace' #simplegui canvas.draw_text() only supports 3 fonts and this was the nicest

    def draw(self, canvas):
        global time
        global counter
        if counter % 60 == 0:
            time = time - 1
        counter = counter - 1
        if time < 0:
            time = 0
        minutes = time // 60
        seconds = time % 60
        timerText = "Time: {0:02}:{1:02}".format(minutes, seconds)
        canvas.draw_text(timerText, [10, 30], self.font_size, self.font_colour, self.font)


Timer = Timer(20, "White") #give it the correct font size here cos idk if you want it bigger or not, also change the colour to whatever you like
frame = simplegui.create_frame("Timer", 500, 700)
frame.set_draw_handler(Timer.draw)
frame.start()