import simplegui

image = simplegui.load_image('https://i.imgur.com/GdpgVw2.png')

width = 1024
height = 512
columns = 8
rows = 4
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
    centre_dest = (21, 63)
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


timer = simplegui.create_timer(45, nextFrame)
timer.start()
frame = simplegui.create_frame('Testing', 42, 126)
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(click)
frame.start()
