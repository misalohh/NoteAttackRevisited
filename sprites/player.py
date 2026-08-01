import pygame
from colours import PLAYER, PLAYER_OUTLINE

class Player:
    def __init__(self, x, y, radius=30):

        self.radius = radius
        self.color = PLAYER

        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, PLAYER , (radius, radius), radius)
        pygame.draw.circle(self.image, PLAYER_OUTLINE, (radius, radius), radius, 4)

        self.rect = self.image.get_rect(center=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)