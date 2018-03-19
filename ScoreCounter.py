try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Player import Player

class ScoreCounter:

    def __init__(self, player):
        self.player = player
        #self.playerScore = str(self.player.scoreCount) <- use for real game

        self.playerScore = str(100) # <- to test



    def update(self, canvas):
        canvas.draw_text("Score: "+ self.playerScore, (10, 30), 20, 'White', 'monospace')

scoretest = ScoreCounter(500)

frame = simplegui.create_frame('Testing', 500, 700)
frame.set_draw_handler(scoretest.update)
frame.start()
