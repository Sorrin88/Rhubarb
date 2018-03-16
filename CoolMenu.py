import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

HEIGHT = 500
WIDTH = 500

class Button:
    def __init__(self, pos, image, active_image, image_center, image_size, action, text, text_size):
        self.pos = pos
        self.image = image
        self.active_image = active_image
        self.image_center = image_center
        self.image_size = image_size
        self.action = action
        self.selected = False
        self.text = text
        self.text_size = text_size

    def draw(self, canvas):
        if not self.selected:
            for b in button_list:
                canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size)
                #draw text on top of button, uses half of text width as offset to centre the text on the button
                canvas.draw_text(self.text, (self.pos[0] - frame.get_canvas_textwidth(self.text, self.text_size)/2, self.pos[1]), self.text_size, 'Black')
        else:
            for b in button_list:
                canvas.draw_image(self.active_image, self.image_center, self.image_size, self.pos, self.image_size)
                canvas.draw_text(self.text, (self.pos[0] - frame.get_canvas_textwidth(self.text, self.text_size) / 2, self.pos[1]), self.text_size, 'Black')

    def activate(self):
        self.action()

    def in_button(self, pos):
            for b in button_list:
                if pos[0] > (self.pos[0] - pos[0]/2)  and pos[0] < (self.pos[0] + (pos[0]/2)):
                    if pos[1] > (self.pos[1] - pos[1]/2) and pos[1] < (self.pos[1] + (pos[1]/2)):
                        self.set_selected(True)

    def get_pos(self):
        return self.pos

    def set_pos(self, p):
        self.pos = p

    def get_action(self):
        return self.action

    def set_action(self, a):
        self.action = a

    def get_selected(self):
        return self.selected

    def set_selected(self, s):
        self.selected = s

    def mouse_handler(self,pos):
        print(pos)
        for b in button_list:
            b.in_button(pos) #for each button in the list, check if the mouseclick is on button or not

#load button images here and name them appropriately and use them to instantiate buttons
image = simplegui.load_image('https://i.imgur.com/WnEVcL4.png') #replace this with actual button image (inactive colour)
active_image = simplegui.load_image('https://i.imgur.com/MDSlp0U.png') #must be identical to inactive button except for colour which should be diff

#define button functions
def play():
    print("button was pressed") #replace with function to start game
    button1.selected = False #call this to stop the function endlessly repeating

def play2():
    print("second button was pressed")
    button2.selected = False #call this to stop the function endlessly repeating

#instantiating buttons
button1 = Button((100, 100), image, active_image, (image.get_width() / 2, image.get_height() / 2),
                 (image.get_width(), image.get_height()), play, "PLAY", 30)
button2 = Button((400, 100), image, active_image, (image.get_width() / 2, image.get_height() / 2),
                 (image.get_width(), image.get_height()), play2, "TEST", 30)
#add buttons to a list
button_list = [button1, button2]

def draw(canvas):
    for b in button_list:
        b.draw(canvas)
        if(b.selected == True):
            b.activate()

frame = simplegui.create_frame("Menu", WIDTH, HEIGHT)
frame.set_mouseclick_handler(button1.mouse_handler)
frame.set_draw_handler(draw)
frame.start()