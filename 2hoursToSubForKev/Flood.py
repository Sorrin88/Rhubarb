try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector


class Flood:

    def __init__(self, player):

        self.pos = Vector(250, 1000)
        self.velocity = Vector(0, 0)

        self.image = simplegui.load_image('https://i.imgur.com/tstIBkD.png')

        self.player = player

    #if we don't want flood to move use this method
    def draw(self, canvas):
        canvas.draw_image(self.image, (250, 37.5), (500, 75), (250, 662.5), (500, 75))





