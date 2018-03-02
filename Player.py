try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
    #
    # def keyDown(self, key):
    #     if key == simplegui.KEY_MAP[Player.right]:
    #         self.right = True
    #         self.left = False
    #
    #     if key == simplegui.KEY_MAP[Player.left]:
    #         self.left = True
    #         self.right = False
    #
    #     if key == simplegui.KEY_MAP[Player.up]:
    #         self.up = True
    #         self.down = False
    #
    #     if key == simplegui.KEY_MAP[Player.down]:
    #         self.down = True
    #         self.up = False

    def keyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.right = False
        if key == simplegui.KEY_MAP['left']:
            self.left = False
        if key == simplegui.KEY_MAP['down']:
            self.down = False
        if key == simplegui.KEY_MAP['up']:
            self.up = False
class Player:

    def __innit__ (self, startingpos, spritesheet, up, left, down, right, lifepoints):
            self.staringPos = startingpos
            self.spriteSheet = spritesheet
            self.up = up
            self.left = left
            self.down = down
            self.right = right
            self.lifePoints = lifepoints
            self.moveRight = False
            self.moveLeft = False
            self.moveUp = False
            self.moveDown = False
    def keyDown(self, key):
        if key == simplegui.KEY_MAP[self.right]:
            self.moveRight = True
            self.moveLeft = False

        if key == simplegui.KEY_MAP[self.left]:
            self.moveLeft = True
            self.moveRight = False

        if key == simplegui.KEY_MAP[self.up]:
            self.moveUp = True
            self.moveDown = False

        if key == simplegui.KEY_MAP[self.down]:
            self.moveDown = True
            self.moveUp = False
    def collide(self):
        pass

    def update(self):
        if Keyboard.right:
            pass
