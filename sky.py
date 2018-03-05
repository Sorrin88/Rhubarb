try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

WIDTH = 400
HEIGHT = 400

position1 = 0
position2 = 401


def draw_handler(canvas):
    global position1
    global position2

    if position1 < HEIGHT + image.get_height()/2:
        canvas.draw_image(image, (200, 200), (400, 400), (200, position1), (400, 400))
        position1 = position1 + 3
    else:
        position1 = -image.get_height()/2

    if position2 < HEIGHT + image.get_height()/2.3:
        canvas.draw_image(image, (200, 200), (400, 400), (200, position2), (400, 400))
        position2 = position2 + 3
    else:

        position2 = -image.get_height() / 2


image = simplegui.load_image('https://i.imgur.com/Trj4fvf.png')

frame = simplegui.create_frame('Testing', WIDTH, HEIGHT)
frame.set_draw_handler(draw_handler)
frame.start()