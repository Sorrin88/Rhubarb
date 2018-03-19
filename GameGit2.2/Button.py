
from Menu import *


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
