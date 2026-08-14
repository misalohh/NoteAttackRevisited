import pygame
from colours import BUTTON, BUTTON_HOVER, BUTTON_OUTLINE, BUTTON_TEXT, SELECTED_BUTTON

class CircleButton:
    def __init__(self, x, y, radius, text):
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)
        self.centre = self.rect.center
        self.radius = radius
        self.text = text
        self.font = pygame.font.Font('assets/Handwriting-Regular.ttf', 70)
        self.color = BUTTON
        self.text_color = BUTTON_TEXT
        self.hover_color = BUTTON_HOVER
        self.selected_color = SELECTED_BUTTON

    def is_hovered(self, mouse_pos):
        dx = mouse_pos[0] - self.centre[0]
        dy = mouse_pos[1] - self.centre[1]
        return (dx ** 2 + dy ** 2) <= self.radius ** 2

    def draw(self, surface, mouse_pos, selected=False):
        if selected:
            color = self.hover_color if self.is_hovered(mouse_pos) else self.selected_color
        elif self.is_hovered(mouse_pos):
            color = self.hover_color
        else:
            color = self.color

        pygame.draw.circle(surface, color, self.centre, self.radius)
        pygame.draw.circle(surface, BUTTON_OUTLINE, self.centre, self.radius, width=3)

        button_text = self.font.render(self.text, True, self.text_color)
        surface.blit(button_text, button_text.get_rect(center=self.centre))

    def is_clicked(self, mouse_pos):
        return self.is_hovered(mouse_pos)