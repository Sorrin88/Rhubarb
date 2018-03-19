try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui




class Level:

    def __init__(self, level):
        self.level = level

    def getLevel(self):
        return self.level
