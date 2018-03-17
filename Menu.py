try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

HEIGHT = 700
WIDTH = 500


class Button:
    def __init__(self, pos, image, active_image, image_center, image_size, action):
        self.pos = pos
        self.image = image
        self.active_image = active_image
        self.image_center = image_center
        self.image_size = image_size
        self.action = action
        self.selected = False

    def draw(self, canvas):
        for b in Menu.button_list:
            if not self.selected:
                canvas.draw_image(self.image, self.image_center, self.image_size, self.pos,
                                  (self.image_size[0] / 2, self.image_size[1] / 2))
            else:
                canvas.draw_image(self.active_image, self.image_center, self.image_size, self.pos,
                                  (self.image_size[0] / 2, self.image_size[1] / 2))

    def activate(self):
        self.action()

    def in_button(self, pos):
        for b in Menu.button_list:
            if pos[0] > (self.pos[0] - self.image_size[0] / 4) and pos[0] < (self.pos[0] + (self.image_size[0] / 4)):
                if pos[1] > (self.pos[1] - self.image_size[1] / 4) and pos[1] < (
                        self.pos[1] + (self.image_size[1] / 4)):
                    self.set_selected(True)

    def set_selected(self, s):
        self.selected = s

    def mouse_handler(self, pos):
        print(pos)
        for b in Menu.button_list:
            b.in_button(pos)  # for each button in the list, check if the mouseclick is on button or not
        for b in Menu.button_list2:
            b.in_button(pos)


class MenuSprite:

    def __init__(self, pos):
        self.pos = pos
        self.spriteSheet = simplegui.load_image('https://i.imgur.com/alQYd7X.png')
        self.spriteSheetWidth = 256
        self.spriteSheetHeight = 256
        self.columns = 2
        self.rows = 2
        self.frameWidth = self.spriteSheetWidth // self.columns
        self.frameHeight = self.spriteSheetHeight // self.rows
        self.frameCentreX = self.frameWidth // 2
        self.frameCentreY = self.frameHeight // 2
        self.frameIndex = (0, 0)
        self.frameCount = 0

    def imgUpdate(self):
        i = (self.frameIndex[0])

        if self.frameCount % 6 == 0:
            i = (self.frameIndex[0] + 1) % self.columns
            if i == 0:
                j = (self.frameIndex[1] + 1) % self.rows
            else:
                j = self.frameIndex[1]

            self.frameIndex = (i, j)

    def draw(self, canvas):
        canvas.draw_image(self.spriteSheet, (self.frameWidth * self.frameIndex[0] + self.frameCentreX,
                                             self.frameHeight * self.frameIndex[1] + self.frameCentreY),
                          (self.frameWidth, self.frameHeight), self.pos, (self.frameWidth, self.frameHeight))
        self.imgUpdate()
        self.frameCount += 1


class Menu:
    def __init__(self):
        self.game_name = simplegui.load_image('https://i.imgur.com/mZmXadK.png')
        self.bg_image = simplegui.load_image('https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/whiteBG.png')
        self.how_to_play_screen = simplegui.load_image(
            'https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/how_to_play_screen.png')

        # loading button images
        self.play_image = simplegui.load_image(
            'https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/playbutton.png')
        self.play_active = simplegui.load_image(
            'https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/playbuttonactive.png')
        self.exit_image = simplegui.load_image(
            'https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/exitbutton.png')
        self.exit_active = simplegui.load_image(
            'https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/exitbuttonactive.png')
        self.how_image = simplegui.load_image('https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/howbutton.png')
        self.how_active = simplegui.load_image(
            'hhttps://raw.githubusercontent.com/Sorrin88/Rhubarb/master/howbuttonactive.png')
        self.back_image = simplegui.load_image(
            'https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/backButton.png')
        self.back_active = simplegui.load_image(
            'https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/backButtonactive.png')

        # instantiating buttons
        self.play_button = Button((100, HEIGHT * 0.75), self.play_image, self.play_active,
                                  (self.play_image.get_width() / 2, self.play_image.get_height() / 2),
                                  (self.play_image.get_width(), self.play_image.get_height()), self.play)
        self.exit_button = Button((400, HEIGHT * 0.75), self.exit_image, self.exit_active,
                                  (self.exit_image.get_width() / 2, self.exit_image.get_height() / 2),
                                  (self.exit_image.get_width(), self.exit_image.get_height()), self.exit)
        self.how_button = Button((250, HEIGHT * 0.75), self.how_image, self.how_active,
                                 (self.how_image.get_width() / 2, self.how_image.get_height() / 2),
                                 (self.how_image.get_width(), self.how_image.get_height()), self.how)
        self.back_button = Button((WIDTH - 70, HEIGHT - 50), self.back_image, self.back_active,
                                  (self.back_image.get_width() / 2, self.back_image.get_height() / 2),
                                  (self.back_image.get_width(), self.back_image.get_height()), self.back)

        self.menuSprite = MenuSprite((WIDTH/2, HEIGHT/2))

        # add buttons to a list
        self.button_list = [self.play_button, self.exit_button, self.how_button]
        self.button_list2 = [
            self.back_button]  # i had to make a second list sorry is this is confusing but hey it works

    # define button functions
    def play(self):
        print("button was pressed")  # replace with function to start game
        self.play_button.selected = False  # call this to stop the function endlessly repeating

    def exit(self):
        print("exit button was pressed")  # replace with code to stop everything running and close window
        self.exit_button.selected = False  # call this to stop the function endlessly repeating

    def how(self):  # when how button pressed draw how to play screen
        frame.set_draw_handler(Menu.drawHowScreen)
        self.how_button.selected = False

    def back(self):  # switch back to menu if back button pressed
        frame.set_draw_handler(Menu.drawMenu)
        self.back_button.selected = False

    def drawHowScreen(self, canvas):
        canvas.draw_image(self.how_to_play_screen, (250, 350), (500, 700), (WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
        self.back_button.draw(canvas)
        if (self.back_button.selected == True):
            self.back_button.activate()

    def drawMenu(self, canvas):
        canvas.draw_image(self.bg_image, (300, 400), (600, 800), (WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

        # KEVIN PUT YOUR CODE FOR LOADING FARMER SPRITE HERE COS IT NEEDS TO DRAW ON TOP OF BACKGOUND IMAGE
        # YEAH SURRE GOTCHA DW

        self.menuSprite.draw(canvas)

        canvas.draw_image(self.game_name, (self.game_name.get_width() / 2, self.game_name.get_height() / 2),
                          (self.game_name.get_width(), self.game_name.get_height()),
                          (WIDTH / 2, HEIGHT / 4), (500, 250))
        for b in self.button_list:
            b.draw(canvas)
            if (b.selected == True):
                b.activate()


# MAIN
Menu = Menu()
frame = simplegui.create_frame("Menu", WIDTH, HEIGHT)
frame.set_mouseclick_handler(Menu.play_button.mouse_handler)
frame.set_draw_handler(Menu.drawMenu)
frame.start()

