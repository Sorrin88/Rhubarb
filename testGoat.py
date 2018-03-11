try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Monster import Monster
goat1 = Monster(Vector(250, 250), xVel, yVel, difficulty, level)

frame = simplegui.create_frame("Half-Life 3",500,500)
frame.set_draw_handler(goat1.update)
frame.start()