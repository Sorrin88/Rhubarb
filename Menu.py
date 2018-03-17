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
        for b in button_list:
            if not self.selected:
                canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, (self.image_size[0]/2, self.image_size[1]/2))
            else:
                canvas.draw_image(self.active_image, self.image_center, self.image_size, self.pos, (self.image_size[0]/2, self.image_size[1]/2))

    def activate(self):
        self.action()

    def in_button(self, pos):
        for b in button_list:
            if pos[0] > (self.pos[0] - self.image_size[0]/4) and pos[0] < (self.pos[0] + (self.image_size[0]/4)):
                if pos[1] > (self.pos[1] - self.image_size[1]/4) and pos[1] < (self.pos[1] + (self.image_size[1]/4)):
                    self.set_selected(True)

    def set_selected(self, s):
        self.selected = s

    def mouse_handler(self,pos):
        print(pos)
        for b in button_list:
            b.in_button(pos) #for each button in the list, check if the mouseclick is on button or not
        for b in button_list2:
            b.in_button(pos)

#loading button images
play_image = simplegui.load_image('https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/playbutton.png')
play_active = simplegui.load_image('https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/playbuttonactive.png')
exit_image = simplegui.load_image('https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/exitbutton.png')
exit_active = simplegui.load_image('https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/exitbuttonactive.png')
how_image = simplegui.load_image('https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/howbutton.png')
how_active = simplegui.load_image('hhttps://raw.githubusercontent.com/Sorrin88/Rhubarb/master/howbuttonactive.png')
back_image = simplegui.load_image('https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/backButton.png')
back_active = simplegui.load_image('https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/backButtonactive.png')

#load game name image and bg image
game_name = simplegui.load_image('https://i.imgur.com/mZmXadK.png')
bg_image = simplegui.load_image('https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/whiteBG.png')
how_to_play_screen = simplegui.load_image('https://raw.githubusercontent.com/Sorrin88/Rhubarb/master/how_to_play_screen.png')

#define button functions
def play():
    print("button was pressed") #replace with function to start game
    play_button.selected = False #call this to stop the function endlessly repeating

def exit():
    print("exit button was pressed") #replace with code to stop everything running and close window
    exit_button.selected = False #call this to stop the function endlessly repeating

def how(): #when how button pressed draw how to play screen
    frame.set_draw_handler(drawHowScreen)
    how_button.selected = False

def back(): #switch back to menu if back button pressed
    frame.set_draw_handler(drawMenu)
    back_button.selected = False

#instantiating buttons
play_button = Button((100, HEIGHT*0.75), play_image, play_active, (play_image.get_width() / 2, play_image.get_height() / 2),
                 (play_image.get_width(), play_image.get_height()), play)
exit_button = Button((400, HEIGHT*0.75), exit_image, exit_active, (exit_image.get_width() / 2, exit_image.get_height() / 2),
                 (exit_image.get_width(), exit_image.get_height()), exit)
how_button = Button((250, HEIGHT*0.75), how_image, how_active, (how_image.get_width() / 2, how_image.get_height() / 2),
                 (how_image.get_width(), how_image.get_height()), how)
back_button = Button((WIDTH - 70, HEIGHT - 50), back_image, back_active, (back_image.get_width() / 2, back_image.get_height() / 2),
                 (back_image.get_width(), back_image.get_height()), back)

#add buttons to a list
button_list = [play_button, exit_button, how_button]
button_list2 = [back_button] # i had to make a second list sorry is this is confusing but hey it works

def drawHowScreen(canvas):
    canvas.draw_image(how_to_play_screen, (250, 350), (500, 700), (WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    back_button.draw(canvas)
    if(back_button.selected == True):
        back_button.activate()

def drawMenu(canvas):
    canvas.draw_image(bg_image, (300, 400), (600, 800), (WIDTH/2, HEIGHT/2), (WIDTH, HEIGHT))
    canvas.draw_text("Kev put the farmer sprite here", (WIDTH/2 - 100, HEIGHT/2), 20, 'Black')

    #KEVIN PUT YOUR CODE FOR LOADING FARMER SPRITE HERE COS IT NEEDS TO DRAW ON TOP OF BACKGOUND IMAGE
    
    canvas.draw_image(game_name, (game_name.get_width() / 2, game_name.get_height() / 2), (game_name.get_width(), game_name.get_height()),
                      (WIDTH/2, HEIGHT/4), (500, 250))
    for b in button_list:
        b.draw(canvas)
        if(b.selected == True):
            b.activate()

frame = simplegui.create_frame("Menu", WIDTH, HEIGHT)
frame.set_mouseclick_handler(play_button.mouse_handler)
frame.set_draw_handler(drawMenu)
frame.start()