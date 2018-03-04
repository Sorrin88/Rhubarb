import simplegui

image = simplegui.load_image('https://i.imgur.com/146hvZf.png')  # farmer invincible left stand

# farmer invincible right stand
# https://i.imgur.com/HxhhRhD.png

width = 384
height = 256
columns = 3
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
    centre_dest = (50, 50)
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


timer = simplegui.create_timer(75, nextFrame)
timer.start()
frame = simplegui.create_frame('Testing', 100, 100)
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(click)
frame.start()
