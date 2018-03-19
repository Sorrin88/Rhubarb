try:
    import simplegui
except:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

class Button:
    def __init__(self, pos, image, active_image, image_center, image_size, action):
        self.pos = pos
        self.image = image
        self.active_image = active_image
        self.image_center = image_center
        self.image_size = image_size
        self.action = action
        self.selected = False

        self.bl1 = list()
        self.bl2 = list()

    def setButtonList1(self, button_list):
        self.bl1 += button_list
    def setButtonList2(self, button_list):
        self.bl2 += button_list

    def draw(self, canvas, button_list):
        for b in button_list:
            if not self.selected:
                canvas.draw_image(self.image, self.image_center, self.image_size, self.pos,
                                  (self.image_size[0] / 2, self.image_size[1] / 2))
            else:
                canvas.draw_image(self.active_image, self.image_center, self.image_size, self.pos,
                                  (self.image_size[0] / 2, self.image_size[1] / 2))

    def activate(self):
        self.action()

    def in_button(self, pos):
        if pos[0] > (self.pos[0] - self.image_size[0] / 4) and pos[0] < (self.pos[0] + (self.image_size[0] / 4)):
            if pos[1] > (self.pos[1] - self.image_size[1] / 4) and pos[1] < (
                    self.pos[1] + (self.image_size[1] / 4)):
                self.set_selected(True)

    def set_selected(self, s):
        self.selected = s

    def mouse_handler(self, pos):
        print(pos)
        for b in self.bl1:
            b.in_button(pos)  # for each button in the list, check if the mouseclick is on button or not
        for b in self.bl2:
            b.in_button(pos)