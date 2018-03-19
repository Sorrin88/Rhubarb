try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

from Player import Player

class ScoreCounter:

    def __init__(self, player):
        self.player = player


        #self.playerScore = str(100) # <- to test



    def update(self, canvas):
        self.playerScore = str(self.player.scoreCount) #<- use for real game
        canvas.draw_text("Score: "+ self.playerScore, (10, 40), 25, 'Black', 'monospace')

##scoretest = ScoreCounter(500)

##frame = simplegui.create_frame('Testing', 500, 700)
##frame.set_draw_handler(scoretest.update)
##frame.start()