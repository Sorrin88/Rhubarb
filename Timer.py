import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

frameRate = 60
time = 90
counter = time * frameRate


def draw(canvas):
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
    canvas.draw_text(timerText, [50, 110], 48, "White")


frame = simplegui.create_frame("Timer", 500, 500)
frame.set_draw_handler(draw)
frame.start()
