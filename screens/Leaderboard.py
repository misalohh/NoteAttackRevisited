import pygame
from UI.Button import Button
from colours import BACKGROUND, TEXT

class Leaderboard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.font = pygame.font.Font('assets/Handwriting-Regular.ttf', 105)
        self.back_button = Button(35, 35, 120, 60, "Back")

    def update(self):
        pass

    def draw(self, surface, mouse_pos):
        surface.fill(BACKGROUND)
        leaderboard_title = self.font.render("Leaderboard", True, TEXT)
        text_rect = leaderboard_title.get_rect(midtop=(self.width // 2, 50))
        surface.blit(leaderboard_title, text_rect)
        self.back_button.draw(surface, mouse_pos)
        
    def handle_click(self, mouse_pos):
        if self.back_button.is_clicked(mouse_pos):
            return "menu"