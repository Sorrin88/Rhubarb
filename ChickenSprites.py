import simplegui

image = simplegui.load_image('https://i.imgur.com/ExUpMNu.png')  # level 1 chicken left walk
# Other chicken spritesheets:

# level 1 chicken right walk:
# https://i.imgur.com/rQ0Yx3V.png

# level 2 chicken left walk:
# https://i.imgur.com/ZaTOq5f.png

# level 2 chicken right walk:
# https://i.imgur.com/hUj9BF0.png

# level 3 chicken left walk:
# https://i.imgur.com/ZwSgQUK.png

# level 3 chicken right walk:
# https://i.imgur.com/T0PwEL3.png

width = 256
height = 128
columns = 2
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
    centre_dest = (53, 53)
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
frame = simplegui.create_frame('Testing', 106, 106)
frame.set_draw_handler(draw_handler)
frame.set_mouseclick_handler(click)
frame.start()
