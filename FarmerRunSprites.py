import simplegui

image = simplegui.load_image('https://i.imgur.com/ovdySX8.png')  # farmer left run
# Other goat spritesheets:

# farmer right run
# https://i.imgur.com/gSUJfWs.png

# farmer left run speedJuiceUp
# https://i.imgur.com/mjSk2zw.png

# farmer right run speedJuiceUp
# https://i.imgur.com/oQQI9TY.png

# farmer left run jumpJuiceUp
# https://i.imgur.com/fDEbrVB.png

# farmer right run jumpJuiceUp
# https://i.imgur.com/eIvA2F8.png

# farmer left run no rake
# https://i.imgur.com/c5oirFa.png

# farmer right run no rake
# https://i.imgur.com/gSUJfWs.png

# farmer left run no rake speedjuiceUp
# https://i.imgur.com/S1PGJIb.png

# farmer right run no rake speedJuiceUp
# https://i.imgur.com/qsEqOMo.png

# farmer left run no rake jumpJuiceUp
# https://i.imgur.com/V0Ggotg.png

# farmer right run no rake jumpJuiceUp
# https://i.imgur.com/58B9wJP.png


width = 256
height = 256
columns = 2
rows = 2
frameWidth = width // columns
frameHeight = height // rows
frameCentreX = frameWidth // 2
frameCentreY = frameHeight // 2
fr_idx = (0, 0)


def drawFrame(canvas):
    x = frameWidth * fr_idx[0] + frameCentreX
    y = frameHeight * fr_idx[1] + frameCentreY
    centre_source = (x, y)
    width_height_source = (frameWidth, frameHeight)
    centre_dest = (60, 60)
    width_height_dest = (frameWidth, frameHeight)
    canvas.draw_image(image, centre_source, width_height_source, centre_dest, width_height_dest)


def draw_handler(canvas):
    drawFrame(canvas)


def nextFrame():
    global fr_idx
    i = (fr_idx[0] + 1) % columns
    if i == 0:
        j = (fr_idx[1] + 1) % rows
    else:
        j = fr_idx[1]
    fr_idx = (i, j)


def click(pos):
    nextFrame()


timer = simplegui.create_timer(100, nextFrame)
timer.start()
frame = simplegui.create_frame('Testing', 120, 120)
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(click)
frame.start()
