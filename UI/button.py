import pygame

class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font('assets/Handwriting-Regular.ttf', 70)
        self.color = (106, 102, 163)
        self.text_color = (221, 216, 184)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        pygame.draw.rect(surface, (221, 216, 184), self.rect, width=3)  
        text_surface = self.font.render(self.text, True, self.text_color)
        surface.blit(text_surface, text_surface.get_rect(center=self.rect.center))

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)