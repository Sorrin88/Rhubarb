import simplegui

image = simplegui.load_image('https://i.imgur.com/ktoQVPl.png')  # level 1 goat left walk
# Other goat spritesheets:

# level 1 goat right walk:
# https://i.imgur.com/OXqA8BM.png

# level 2 goat left walk:
# https://i.imgur.com/1ZoBw5C.png

# level 2 goat right walk
# https://i.imgur.com/ec1ldkO.png

# level 3 goat left walk
# https://i.imgur.com/XItJi98.png

# level 3 goat right walk
# https://i.imgur.com/R7wftgH.png

width = 384
height = 128
columns = 3
rows = 1
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
    centre_dest = (59, 59)
    width_height_dest = (frameWidth, frameHeight)
    canvas.draw_image(image, centre_source, width_height_source, centre_dest, width_height_dest)


def draw_handler(canvas):
    drawFrame(canvas)


def nextFrame():
    global fr_idx
    i = (fr_idx[0] + 1) % columns
    fr_idx = (i, 0)


def click(pos):
    nextFrame()


timer = simplegui.create_timer(100, nextFrame)
timer.start()
frame = simplegui.create_frame('Testing', 118, 118)
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(click)
frame.start()
