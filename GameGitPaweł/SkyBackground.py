try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

IMAGEWIDTH = 500
IMAGEHEIGHT = 1000

position1 = -500
position2 = 500
timer = 0


def draw_handler(canvas):
    global position1
    global position2
    global timer

    if position1 < IMAGEHEIGHT:
        if timer % 3 == 0:
            canvas.draw_image(image, (IMAGEWIDTH / 2, IMAGEHEIGHT / 2), (IMAGEWIDTH, IMAGEHEIGHT),
                              (IMAGEWIDTH / 2, position1), (IMAGEWIDTH, IMAGEHEIGHT))
            position1 = position1 + 1
            timer = timer + 1
        else:
            canvas.draw_image(image, (IMAGEWIDTH / 2, IMAGEHEIGHT / 2), (IMAGEWIDTH, IMAGEHEIGHT),
                              (IMAGEWIDTH / 2, position1), (IMAGEWIDTH, IMAGEHEIGHT))
            timer = timer + 1
    else:
        canvas.draw_image(image, (IMAGEWIDTH / 2, IMAGEHEIGHT / 2), (IMAGEWIDTH, IMAGEHEIGHT),
                          (IMAGEWIDTH / 2, position1), (IMAGEWIDTH, IMAGEHEIGHT))
        position1 = -500

    if position2 < IMAGEHEIGHT:
        if timer % 3 == 0:
            canvas.draw_image(image, (IMAGEWIDTH / 2, IMAGEHEIGHT / 2), (IMAGEWIDTH, IMAGEHEIGHT),
                              (IMAGEWIDTH / 2, position2), (IMAGEWIDTH, IMAGEHEIGHT))
            position2 = position2 + 1
            timer = timer + 1
        else:
            canvas.draw_image(image, (IMAGEWIDTH / 2, IMAGEHEIGHT / 2), (IMAGEWIDTH, IMAGEHEIGHT),
                              (IMAGEWIDTH / 2, position2), (IMAGEWIDTH, IMAGEHEIGHT))
            timer = timer + 1
    else:
        canvas.draw_image(image, (IMAGEWIDTH / 2, IMAGEHEIGHT / 2), (IMAGEWIDTH, IMAGEHEIGHT),
                          (IMAGEWIDTH / 2, position2), (IMAGEWIDTH, IMAGEHEIGHT))
        position2 = -500

#if level = 1....
image = simplegui.load_image('https://i.imgur.com/VLZsdso.png')
#else image = simplegui.load_image(another image link)

frame = simplegui.create_frame('Sky', IMAGEWIDTH, IMAGEHEIGHT / 2)
frame.set_draw_handler(draw_handler)
frame.start()