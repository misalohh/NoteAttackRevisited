from colours import BACKGROUND
from UI.button import Button

class Gameplay:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.back_button = Button(35, 35, 120, 60, "Back")

    def update(self):
        pass

    def draw(self, surface, mouse_pos):
        surface.fill(BACKGROUND)
        self.back_button.draw(surface, mouse_pos)

    def handle_click(self, mouse_pos):
            if self.back_button.is_clicked(mouse_pos):
                return "menu"