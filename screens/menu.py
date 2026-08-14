import pygame
from UI.Button import Button
from UI.CircleButton import CircleButton
from colours import BACKGROUND, TEXT

class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font('assets/Handwriting-Regular.ttf', 105)

        self.start_button = Button(width // 2 - 175, 170, 350, 80, "Start")
        self.rules_button = Button(width // 2 - 175, 270, 350, 80, "Rules")
        self.settings_button = Button(width // 2 - 175, 370, 350, 80, "Settings")

        self.leaderboard_button = CircleButton(width // 2 - 175, 470, 40, "Leaderboard")
        self.exit_button = CircleButton(width // 2 + 135, 470, 40, "Exit")

    def update(self):
        pass

    def draw(self, surface, mouse_pos):
        surface.fill(BACKGROUND)
        menu_title = self.font.render("Note Attack Revisited", True, TEXT)
        text_rect = menu_title.get_rect(midtop=(self.width // 2, 50))
        surface.blit(menu_title, text_rect)

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