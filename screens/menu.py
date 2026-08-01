import pygame
from UI.button import Button
from colours import BACKGROUND, TEXT

class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font('assets/Handwriting-Regular.ttf', 105)

        self.start_button = Button(width // 2 - 175, 170, 350, 80, "Start")
        self.rules_button = Button(width // 2 - 175, 270, 350, 80, "Rules")
        self.settings_button = Button(width // 2 - 175, 370, 350, 80, "Settings")

    def update(self):
        pass

    def draw(self, surface, mouse_pos):
        surface.fill(BACKGROUND)
        text_surface = self.font.render("Note Attack Revisited", True, TEXT)
        text_rect = text_surface.get_rect(midtop=(self.width // 2, 50))
        surface.blit(text_surface, text_rect)

        self.start_button.draw(surface, mouse_pos)
        self.rules_button.draw(surface, mouse_pos)
        self.settings_button.draw(surface, mouse_pos)

    def handle_click(self, mouse_pos):
        if self.start_button.is_clicked(mouse_pos):
            return "game"
        if self.rules_button.is_clicked(mouse_pos):
            return "rules"
        if self.settings_button.is_clicked(mouse_pos):
            return "settings"
        return None