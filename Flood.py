try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Vector import Vector


class Flood:

    def __init__(self, difficulty, player):

        self.pos = Vector(250, 1000)
        self.velocity = Vector(0, 0)

        self.image = simplegui.load_image('https://i.imgur.com/8FnmykN.png')

        self.difficulty = difficulty

        if difficulty == 'easy':
            self.slow = 8
        elif difficulty == 'medium':
            self.slow = 5
        elif difficulty == 'hard':
            self.slow = 3

        self.player = player
        self.counter = 0

    def collide(self):
        # if interact game over
        pass

    #if we want flood to move use this method...
    def update(self, canvas):
        # while interaction with player == False:
        canvas.draw_image(self.image, (250, 350), (500, 700), self.pos.getP(), (500, 700))
        if self.counter % self.slow == 0:
            self.velocity = Vector(0, -1)
            self.pos.add(self.velocity)
        self.counter += 1

    #if we don't want flood to move use this method
    def draw(self, canvas):
        canvas.draw_image(self.image, (250, 350), (500, 700), self.pos.getP(), (500, 700))


def draw(canvas):
    flood.draw(canvas)


flood = Flood('hard', 'p')

frame = simplegui.create_frame("Half-Life 3", 500, 700)
frame.set_draw_handler(draw)
frame.start()
