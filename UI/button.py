import pygame
from colours import BUTTON, BUTTON_TEXT, BUTTON_OUTLINE, BUTTON_HOVER

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font('assets/Handwriting-Regular.ttf', 70)
        self.color = BUTTON
        self.text_color = BUTTON_TEXT
        self.hover_color = BUTTON_HOVER

    def draw(self, surface, mouse_pos):
        hover = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(surface, hover, self.rect)
        pygame.draw.rect(surface, BUTTON_OUTLINE, self.rect, width=3)  
        text_surface = self.font.render(self.text, True, self.text_color)
        surface.blit(text_surface, text_surface.get_rect(center=self.rect.center))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)