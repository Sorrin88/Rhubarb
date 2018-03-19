from Menu import *

frame = simplegui.create_frame("Menu", WIDTH, HEIGHT)
Menu = Menu(frame)

frame.set_mouseclick_handler(Menu.play_button.mouse_handler)
frame.set_draw_handler(Menu.drawMenu)
if (Menu.how()):
    frame.set_draw_handler(Menu.drawHowScreen)
frame.start()