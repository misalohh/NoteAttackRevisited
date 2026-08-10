import pygame
from screens import gameplay
from UI.button import Button
from colours import BACKGROUND, TEXT

class Settings:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font('assets/Handwriting-Regular.ttf', 105)

        self.back_button = Button(35, 35, 120, 60, "Back")
        self.easy_button = Button(width // 2 - 175, 170, 350, 80, "Easy")
        self.medium_button = Button(width // 2 - 175, 270, 350, 80, "Medium")
        self.hard_button = Button(width // 2 - 175, 370, 350, 80, "Hard")

        self.selected_difficulty = "medium"

    def update(self):
        pass

    def draw(self, surface, mouse_pos):
        surface.fill(BACKGROUND)
        settings_title = self.font.render("Settings", True, TEXT)
        text_rect = settings_title.get_rect(midtop=(self.width // 2, 50))
        surface.blit(settings_title, text_rect)

        self.back_button.draw(surface, mouse_pos)
        self.easy_button.draw(surface, mouse_pos, selected=self.selected_difficulty == "easy")
        self.medium_button.draw(surface, mouse_pos, selected=self.selected_difficulty == "medium")
        self.hard_button.draw(surface, mouse_pos, selected=self.selected_difficulty == "hard")

    def handle_click(self, mouse_pos):
            if self.back_button.is_clicked(mouse_pos):
                return "menu"
            if self.easy_button.is_clicked(mouse_pos):
                self.selected_difficulty = "easy"
                self.gameplay.spawn_interval = 250
            if self.medium_button.is_clicked(mouse_pos):
                self.selected_difficulty = "medium"
                self.gameplay.spawn_interval = 170
            if self.hard_button.is_clicked(mouse_pos):
                self.selected_difficulty = "hard"
                self.gameplay.spawn_interval = 100
            return None

        