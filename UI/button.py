import pygame
from colours import BUTTON, BUTTON_TEXT, BUTTON_OUTLINE, BUTTON_HOVER, SELECTED_BUTTON

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font('assets/Handwriting-Regular.ttf', 70)
        self.color = BUTTON
        self.text_color = BUTTON_TEXT
        self.hover_color = BUTTON_HOVER
        self.selected_color = SELECTED_BUTTON

    def draw(self, surface, mouse_pos, selected=False):
        if selected:
            color = self.selected_color
            if self.rect.collidepoint(mouse_pos):
                color = self.hover_color
        elif self.rect.collidepoint(mouse_pos):
            color = self.hover_color
        else:
            color = self.color
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, BUTTON_OUTLINE, self.rect, width=3)  
        button_text = self.font.render(self.text, True, self.text_color)
        surface.blit(button_text, button_text.get_rect(center=self.rect.center))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)